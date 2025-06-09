# Copied and edited from https://github.com/ckan/ckan/blob/2.11/ckan/views/group.py
# encoding: utf-8
from __future__ import annotations

import logging
from collections import OrderedDict
from typing import Any, Optional, Union

from urllib.parse import urlencode
import csv
from io import StringIO

import ckan.lib.base as base
from ckan.lib.helpers import helper_functions as h
from ckan.lib.helpers import Page
import ckan.lib.navl.dictization_functions as dict_fns
import ckan.logic as logic
import ckan.lib.search as search
import ckan.model as model
import ckan.authz as authz
import ckan.lib.plugins as lib_plugins
import ckan.plugins as plugins
from ckan.common import g, config, request, current_user, _
from ckan.views.home import CACHE_PARAMETERS
from ckan.views.dataset import _get_search_details

from flask import Blueprint, make_response
from flask.views import MethodView
from flask.wrappers import Response
from ckan.types import Context, DataDict, Schema


NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
ValidationError = logic.ValidationError
check_access = logic.check_access
get_action = logic.get_action
tuplize_dict = logic.tuplize_dict
clean_dict = logic.clean_dict
parse_params = logic.parse_params

log = logging.getLogger(__name__)

lookup_group_plugin = lib_plugins.lookup_group_plugin
lookup_group_controller = lib_plugins.lookup_group_controller


def _get_group_template(template_type: str,
                        group_type: Optional[str] = None) -> str:
    group_plugin = lookup_group_plugin(group_type)
    method = getattr(group_plugin, template_type)
    try:
        return method(group_type)
    except TypeError as err:
        if u'takes 1' not in str(err) and u'takes exactly 1' not in str(err):
            raise
        return method()


def _db_to_form_schema(group_type: Optional[str] = None) -> Schema:
    u'''This is an interface to manipulate data from the database
     into a format suitable for the form (optional)'''
    return lookup_group_plugin(group_type).db_to_form_schema()


def _setup_template_variables(context: Context,
                              data_dict: DataDict,
                              group_type: Optional[str] = None) -> None:
    if u'type' not in data_dict:
        data_dict[u'type'] = group_type
    return lookup_group_plugin(group_type).\
        setup_template_variables(context, data_dict)


def _force_reindex(grp: dict[str, Any]) -> None:
    u''' When the group name has changed, we need to force a reindex
    of the datasets within the group, otherwise they will stop
    appearing on the read page for the group (as they're connected via
    the group name)'''
    group = model.Group.get(grp['name'])
    assert group
    for dataset in group.packages():
        search.rebuild(dataset.name)


def _guess_group_type(expecting_name: bool = False) -> str:
    u"""
            Guess the type of group from the URL.
            * The default url '/group/xyz' returns None
            * group_type is unicode
            * this handles the case where there is a prefix on the URL
              (such as /data/organization)
        """
    parts: list[str] = request.path.split(u'/')
    parts = [x for x in parts if x]

    idx = 0
    if expecting_name:
        idx = -1

    gt = parts[idx]

    return gt

class CreateGroupView(MethodView):
    u'''Create group view '''

    def _prepare(
            self,
            is_organization: bool,
            data: Optional[dict[str, Any]] = None) -> Context:
        if data and u'type' in data:
            group_type = data['type']
        else:
            group_type = _guess_group_type()
        if data:
            data['type'] = group_type

        context: Context = {
            u'user': current_user.name,
            u'save': u'save' in request.args,
            u'parent': request.args.get(u'parent', None),
            u'group_type': group_type
        }

        try:
            action_name = (
                'organization_create' if is_organization else 'group_create'
            )
            check_access(action_name, context)
        except NotAuthorized:
            base.abort(403, _(u'Unauthorized to create a group'))

        return context

    def post(self, group_type: str,
             is_organization: bool) -> Union[Response, str]:
        context = self._prepare(is_organization)
        try:
            data_dict = clean_dict(
                dict_fns.unflatten(tuplize_dict(parse_params(request.form))))
            data_dict.update(clean_dict(
                dict_fns.unflatten(tuplize_dict(parse_params(request.files)))
            ))
        except dict_fns.DataError:
            base.abort(400, _(u'Integrity Error'))
        user = current_user.name
        data_dict['type'] = group_type or u'group'
        data_dict['users'] = [{u'name': user, u'capacity': u'admin'}]
        try:
            action_name = (
                'organization_create' if is_organization else 'group_create'
            )
            group = get_action(action_name)(context, data_dict)
        except (NotFound, NotAuthorized):
            base.abort(404, _(u'Group not found'))
        except ValidationError as e:
            errors = e.error_dict
            error_summary = e.error_summary
            if data_dict.get(u'url_type') == 'upload':
                data_dict[u'url_type'] = ''
                data_dict[u'previous_upload'] = True
                data_dict[u'doc_url'] = ''
                data_dict[u'image_url'] = ''
                data_dict[u'sstp_doc_document_upload'] = ''
                data_dict[u'srti_doc_document_upload'] = ''
                data_dict[u'rtti_doc_document_upload'] = ''
                data_dict[u'proxy_pdf_url'] = ''
            return self.get(group_type, is_organization,
                            data_dict, errors, error_summary)

        return h.redirect_to(
            group['type'] + '.read', id=group['name'])

    def get(self,
            group_type: str,
            is_organization: bool,
            data: Optional[dict[str, Any]] = None,
            errors: Optional[dict[str, Any]] = None,
            error_summary: Optional[dict[str, Any]] = None) -> str:
        context = self._prepare(is_organization)
        data = data or clean_dict(
            dict_fns.unflatten(
                tuplize_dict(
                    parse_params(request.args, ignore_keys=CACHE_PARAMETERS)
                )
            )
        )

        if not data.get(u'image_url', u'').startswith(u'http'):
            data.pop(u'image_url', None)
        errors = errors or {}
        error_summary = error_summary or {}
        extra_vars: dict[str, Any] = {
            u'data': data,
            u'errors': errors,
            u'error_summary': error_summary,
            u'action': u'new',
            u'group_type': group_type
        }
        _setup_template_variables(
            context, data, group_type=group_type)
        form = base.render(
            _get_group_template(u'group_form', group_type), extra_vars)

        # TODO: Remove
        # ckan 2.9: Adding variables that were removed from c object for
        # compatibility with templates in existing extensions
        g.form = form

        extra_vars["form"] = form
        return base.render(
            _get_group_template(u'new_template', group_type), extra_vars)


class EditGroupView(MethodView):
    u''' Edit group view'''

    def _prepare(self, is_organization: bool, id: Optional[str]) -> Context:
        data_dict: dict[str, Any] = {u'id': id, u'include_datasets': False}

        context: Context = {
            u'user': current_user.name,
            u'save': u'save' in request.args,
            u'for_edit': True,
            u'parent': request.args.get(u'parent', None),
            u'id': id
        }

        try:
            action_name = (
                'organization_show' if is_organization else 'group_show'
            )
            get_action(action_name)(context, data_dict)

            action_name = (
                'organization_update' if is_organization else 'group_update'
            )
            check_access(action_name, context, data_dict)
        except NotAuthorized:
            base.abort(403, _(u'Unauthorized to create a group'))
        except NotFound:
            base.abort(404, _(u'Group not found'))

        return context

    def post(self,
             group_type: str,
             is_organization: bool,
             id: Optional[str] = None) -> Union[Response, str]:
        context = self._prepare(is_organization, id=id)
        try:
            data_dict = clean_dict(
                dict_fns.unflatten(tuplize_dict(parse_params(request.form))))
            data_dict.update(clean_dict(
                dict_fns.unflatten(tuplize_dict(parse_params(request.files)))
            ))
        except dict_fns.DataError:
            base.abort(400, _(u'Integrity Error'))
        data_dict['id'] = context['id']
        context['allow_partial_update'] = True
        try:
            action_name = (
                'organization_show' if is_organization else 'group_show'
            )
            group_data = get_action(action_name)(context, data_dict)
            action_name = (
                'organization_update' if is_organization else 'group_update'
            )
            group = get_action(action_name)(context, data_dict)
            if id != group['name']:
                _force_reindex(group)
        except (NotFound, NotAuthorized):
            base.abort(404, _(u'Group not found'))
        except ValidationError as e:
            errors = e.error_dict
            error_summary = e.error_summary
            if data_dict.get('url_type') == 'upload':
                def entry_is_updated(entry_key):
                    return (
                        entry_key in group_data 
                        and entry_key in data_dict 
                        and group_data[entry_key] != data_dict[entry_key]
                    )

                data_dict['url_type'] = ''
                data_dict['previous_upload'] = True
                for entry_key in [
                    'image_url', 
                    'rtti_doc_document_upload', 
                    'sstp_doc_document_upload', 
                    'srti_doc_document_upload', 
                    'proxy_pdf_url'
                ]:
                    data_dict[entry_key] = (
                        '' 
                        if entry_is_updated(entry_key) 
                        else group_data.get(entry_key, '')
                    )
            assert id
            return self.get(id, group_type, is_organization,
                            data_dict, errors, error_summary)
        return h.redirect_to(
            group['type'] + '.read', id=group[u'name'])

    def get(self,
            id: str,
            group_type: str,
            is_organization: bool,
            data: Optional[dict[str, Any]] = None,
            errors: Optional[dict[str, Any]] = None,
            error_summary: Optional[dict[str, Any]] = None) -> str:
        context = self._prepare(is_organization, id=id)
        data_dict: dict[str, Any] = {u'id': id, u'include_datasets': False}
        try:
            action_name = (
                'organization_show' if is_organization else 'group_show'
            )
            group_dict = get_action(action_name)(context, data_dict)
        except (NotFound, NotAuthorized):
            base.abort(404, _(u'Group not found'))
        data = data or group_dict
        assert data is not None
        errors = errors or {}
        extra_vars: dict[str, Any] = {
            u'data': data,
            u"group_dict": group_dict,
            u'errors': errors,
            u'error_summary': error_summary,
            u'action': u'edit',
            u'group_type': group_type
        }

        _setup_template_variables(context, data, group_type=group_type)
        form = base.render(
            _get_group_template(u'group_form', group_type), extra_vars)

        # TODO: Remove
        # ckan 2.9: Adding variables that were removed from c object for
        # compatibility with templates in existing extensions
        g.grouptitle = group_dict.get(u'title')
        g.groupname = group_dict.get(u'name')
        g.data = data
        g.group_dict = group_dict

        extra_vars["form"] = form
        return base.render(
            _get_group_template(u'edit_template', group_type), extra_vars)

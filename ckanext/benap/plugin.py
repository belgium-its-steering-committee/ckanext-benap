# coding=utf-8
from collections import OrderedDict

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation
import json

from ckanext.benap.helpers import ontology_helper, scheming_language_text_fallback, json_loads, \
    package_notes_translated_fallback, field_translated_fallback, organisation_names_for_autocomplete, \
    get_translated_tags, scheming_language_text, format_datetime, get_translated_tag, get_translated_tag_with_name, \
    forum_url, filter_default_tags_only, getTranslatedVideoUrl, show_element, get_organization_by_id, benap_fluent_label, \
    translate_organization_filter, is_user_sysAdmin, is_nap_checked, convert_validation_list_to_JSON
from ckanext.benap.util.forms import map_for_form_select
from ckanext.benap.validators import phone_number_validator, \
    countries_covered_belgium, is_after_start, https_validator, modified_by_sysadmin, \
    is_choice_null
from ckanext.benap.logic.auth.get import user_list


class BenapPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)
    plugins.implements(plugins.IValidators, inherit=True)
    plugins.implements(plugins.IAuthFunctions, inherit=False)
    plugins.implements(plugins.IFacets, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)

    geographic_granularity_map = [('', ''),
                                  ('national', 'National'),
                                  ('regional', 'Regional'),
                                  ('province', 'province-'),
                                  ('municipality', 'municipality'),
                                  ('other', 'other')]

    _validators = {}

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'benap')
        toolkit.add_resource('fanstatic', 'nap_checked_pill_style.css')

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'benap_geographic_granularity_helper': lambda context: map_for_form_select(self.geographic_granularity_map),
            'benap_ontology_helper': ontology_helper,
            'benap_scheming_language_text_fallback': scheming_language_text_fallback,
            'benap_package_notes_translated_fallback': package_notes_translated_fallback,
            'benap_field_translated_fallback': field_translated_fallback,
            'json_loads': json_loads,
            'benap_organisation_names_for_autocomplete': organisation_names_for_autocomplete,
            'get_translated_tag_with_name': get_translated_tag_with_name,
            'get_translated_tags': get_translated_tags,
            'get_translated_tag': get_translated_tag,
            'filter_default_tags_only': filter_default_tags_only,
            'benap_scheming_language_text': scheming_language_text,
            'format_datetime': format_datetime,
            'benap_forum_url': forum_url,
            'getTranslatedVideoUrl': getTranslatedVideoUrl,
            'benap_get_organization_by_id': get_organization_by_id,
            'translate_organization_filter': translate_organization_filter,
            'show_element': show_element,
            'benap_fluent_label': benap_fluent_label,
            'benap_is_user_sysAdmin': is_user_sysAdmin,
            'benap_is_nap_checked':is_nap_checked,
            'benap_convert_validation_list_to_JSON': convert_validation_list_to_JSON
        }

    # IValidators

    def get_validators(self):
        return {
            'phone_number_validator': phone_number_validator,
            'benap_countries_covered_belgium': countries_covered_belgium,
            'benap_is_after_start': is_after_start,
            'benap_https_validator': https_validator,
            'benap_modified_by_sysadmin': modified_by_sysadmin,
            'benap_is_choice_null': is_choice_null
        }

    # IAuthFunctions

    def get_auth_functions(self):
        return {
            'user_list': user_list,
        }

    # IFacets
    def dataset_facets(self, facets_dict, package_type):
        facets_dict = OrderedDict([
            (u'nap_type', u'NAP Type'),
            (u'its_dataset_type', u'Dataset Type'),
            (u'tags', u'Tags'),
            (u'regions_covered', u'Area covered by publication'),
            (u'organization', u'Organizations'),
            (u'res_format', u'Formats'),
            (u'license_id', u'Licenses'),
        ])
        return facets_dict

    # IPackageController
    def before_index(self, pkg_dict):
        if "regions_covered" in pkg_dict:
            pkg_dict["regions_covered"] = json.loads(pkg_dict["regions_covered"])
        if "nap_type" in pkg_dict:
            pkg_dict["nap_type"] = json.loads(pkg_dict["nap_type"])
        if "its_dataset_type" in pkg_dict:
            try:
                ## only when validation is used in json schema is next fct needed
                converted_list = convert_validation_list_to_JSON(pkg_dict["its_dataset_type"])
                pkg_dict["its_dataset_type"] = json.loads(converted_list)
            except Exception:
                pkg_dict["its_dataset_type"] = json.loads(pkg_dict["its_dataset_type"])

        return pkg_dict

    def before_view(self, pkg_dict):
        pkg_dict.pop('agreement_declaration_nap', None)
        return pkg_dict

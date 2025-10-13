# coding=utf-8
from collections import OrderedDict

from ckan import authz
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.plugins.toolkit import _
from ckan.lib.plugins import DefaultTranslation
import json
from flask import Blueprint, send_from_directory
from ckan.common import current_user

from ckanext.benap.helpers import ontology_helper, organization_name, organisation_names_for_autocomplete, \
    get_translated_tags, scheming_language_text, format_datetime, ckan_tag_to_transport_mode_concept_label,\
    parse_embedded_links, organization_name_by_id, lang_text, \
    benap_get_organization_field_by_id,\
    benap_get_organization_field_by_specified_field, benap_retrieve_dict_items_or_keys_or_values, get_translated_category_and_sub_category, \
    benap_retrieve_org_title_tel_email, benap_retrieve_raw_choices_list, benap_tag_update_helper, _c, is_member_of_org, get_facet_label_function, get_facet_name_label_function

from ckanext.benap.util.forms import map_for_form_select
from ckanext.benap.logic.validators import doc_validator, logo_extensions, phone_number_validator, \
    countries_covered_belgium, is_after_start, https_validator, modified_by_sysadmin, \
    is_choice_null, contact_point_org_fields_consistency_check, \
    license_fields_conditional_validation, benap_tag_string_convert, fluent_tags_validator, category_sub_category_validator
from ckanext.benap.helpers.concepts import get_concept_label

from ckanext.benap.logic.auth.get import member_list, user_autocomplete, user_list
from ckanext.benap.custom_group import CreateGroupView, EditGroupView
from ckanext.benap.uploader import OrganizationUploader, organization_storage_dir


@plugins.toolkit.blanket.actions # auto register all actions in logic/action.py
class BenapPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)
    plugins.implements(plugins.IValidators, inherit=True)
    plugins.implements(plugins.IAuthFunctions, inherit=False)
    plugins.implements(plugins.IFacets, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IBlueprint, inherit=True)
    plugins.implements(plugins.IUploader, inherit=True)

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
        toolkit.add_resource('assets', 'benap')

    # ITemplateHelpers

    def get_helpers(self):
        return {
            '_c': _c,
            'benap_geographic_granularity_helper': lambda context: map_for_form_select(self.geographic_granularity_map),
            'benap_ontology_helper': ontology_helper,
            'benap_organisation_names_for_autocomplete': organisation_names_for_autocomplete,
            'benap_lang_text': lang_text,
            'get_translated_tags': get_translated_tags,
            'ckan_tag_to_transport_mode_concept_label': ckan_tag_to_transport_mode_concept_label,
            'benap_scheming_language_text': scheming_language_text,
            'format_datetime': format_datetime,
            'benap_organization_name': organization_name,
            'benap_organization_name_by_id': organization_name_by_id,
            'benap_get_organization_field_by_id': benap_get_organization_field_by_id,
            'benap_get_organization_field_by_specified_field': benap_get_organization_field_by_specified_field,
            'benap_retrieve_dict_items_or_keys_or_values': benap_retrieve_dict_items_or_keys_or_values,
            'benap_get_translated_category_and_sub_category': get_translated_category_and_sub_category,
            'benap_retrieve_org_title_tel_email': benap_retrieve_org_title_tel_email,
            'benap_retrieve_raw_choices_list': benap_retrieve_raw_choices_list,
            'benap_tag_update_helper': benap_tag_update_helper,
            'benap_parse_embedded_links': parse_embedded_links,
            'benap_is_member_of_org': is_member_of_org,
            'get_facet_name_label_function': get_facet_name_label_function,
            'get_facet_label_function': get_facet_label_function,
        }

    # IValidators

    def get_validators(self):
        return {
            'phone_number_validator': phone_number_validator,
            'benap_countries_covered_belgium': countries_covered_belgium,
            'benap_is_after_start': is_after_start,
            'benap_https_validator': https_validator,
            'benap_modified_by_sysadmin': modified_by_sysadmin,
            'benap_is_choice_null': is_choice_null,
            'benap_contact_point_org_fields_consistency_check': contact_point_org_fields_consistency_check,
            'benap_license_fields_conditional_validation': license_fields_conditional_validation,
            'benap_tag_string_convert': benap_tag_string_convert,
            'benap_fluent_tags_validator': fluent_tags_validator,
            'benap_category_sub_category_validator': category_sub_category_validator,
            'benap_logo_extensions': logo_extensions,
            'benap_doc_validator': doc_validator,
        }

    # IAuthFunctions

    def get_auth_functions(self):
        return {
            'user_list': user_list,
            'user_autocomplete': user_autocomplete,
            'member_list': member_list,
        }

    # IFacets
    def dataset_facets(self, facets_dict, package_type):
        # This overrides the full facets list, which is not recommended by the docs, as the order
        # that plugins add facets now matters. However, the assumption that this is done 
        # is too far coupled in code too easily factor away. So leave this for now.
        facets_dict = OrderedDict([
            ('nap_type', _('NAP Type')),
            ('tags', _('Transportation modes')),
            ('regions_covered_uri', _('Area covered by publication')),
            ('mobility_theme_uri', _('Mobility Theme')),
            ('license_uri', _('License')),
            ('format_uri', _('Format')),
            ('organization', _('Organizations')),
        ])
        return facets_dict

    # IBlueprint
    def get_blueprint(self):
        '''
        Was required for something called uploadFix and copied from here
        https://github.com/belgium-its-steering-committee/ckanext-scheming/blob/MobilityDCAT/root/ckanext/scheming/controllers/customGroup.py#L134-L135
        Is required for multiple uploads on the organization create/edit page
        '''
        blueprint = Blueprint(
            'organization_custom', 
            __name__,
            url_prefix='/organization',
            url_defaults={
                'group_type': 'organization',
                'is_organization': True
            }
        )

        blueprint.add_url_rule(
            '/new',
            view_func=CreateGroupView.as_view('new'),
            methods=['GET', 'POST']
        )

        blueprint.add_url_rule(
            '/edit/<id>',
            view_func=EditGroupView.as_view('edit'),
            methods=['GET', 'POST']
        )
        
        # Intercept GET /uploads/organization to specify file access rights for org files
        # Alternatively IMiddleware could also work
        files_access_blueprint = Blueprint(
            'files_access_intercept',
            __name__,
            url_prefix='/uploads/organization'
        )

        def _check_org_file_rights(org_id, file_id):
          logo_filename = benap_get_organization_field_by_id(org_id, 'image_url')
          user_id = getattr(current_user, 'id', None)
          if not (logo_filename == file_id # public access for organization logo
                  or authz.has_user_permission_for_group_or_org(org_id, user_id, 'read') 
                  or user_id == 'napcontrolbody'):
            toolkit.abort(404)

          org_directory = organization_storage_dir(org_id)
          if not org_directory:
            toolkit.abort(404)

          return send_from_directory(org_directory, file_id)

        files_access_blueprint.add_url_rule(
            '/<org_id>/<file_id>',
            view_func=_check_org_file_rights,
            methods=['GET']
        )

        return [blueprint, files_access_blueprint]

    # IPackageController
    def before_dataset_index(self, pkg_dict):
        # TODO: Are some of these labels meant to be searchable? If so, consider multilang indexing?
        # Currently only english labels are indexed
        if "regions_covered" in pkg_dict:
            pkg_dict["regions_covered_uri"] = json.loads(pkg_dict["regions_covered"])
            pkg_dict["regions_covered_label"] = list(map(lambda uri: get_concept_label(uri, 'en'), json.loads(pkg_dict["regions_covered"])))
        if "mobility_theme" in pkg_dict:
            # 2 lvl concept scheme
            mob_theme_dict = json.loads(pkg_dict["mobility_theme"])
            mob_themes = []
            for broader_theme_uri, narrower_themes in mob_theme_dict.items():
                mob_themes.append(broader_theme_uri)
                mob_themes = mob_themes + narrower_themes
            pkg_dict["mobility_theme_uri"] = mob_themes
            pkg_dict["mobility_theme_label"] = list(map(lambda uri: get_concept_label(uri, 'en'), mob_themes))
        resources = json.loads(pkg_dict["data_dict"])["resources"]
        if resources:
            formats = [res.get("format") for res in resources if res.get("format")]
            pkg_dict["format_uri"] = list(set(formats))  # uniquify
            licenses = [res.get("license_type") for res in resources if res.get("license_type")]
            pkg_dict["license_uri"] = list(set(licenses))  # uniquify
        if "nap_type" in pkg_dict:
            pkg_dict["nap_type"] = json.loads(pkg_dict["nap_type"])

        return pkg_dict

    def before_dataset_view(self, pkg_dict):
        # Remove 'agreement_declaration_nap' from the dictionary if it exists
        pkg_dict.pop('agreement_declaration_nap', None)

        # Get the organization ID associated with the dataset
        org_id = pkg_dict.get('organization', {}).get('id')

        org_data = toolkit.get_action('organization_show')(
            {}, 
            {
                'id': org_id,
                'include_dataset_count': False,
                'include_users': False,
                'include_groups': False,
                'include_tags': False,
                'include_followers': False,
            }
        )

        # Update package dictionary with organization details and publisher name
        pkg_dict.update({
            'publisher_url': org_data.get('do_website'),
            'publisher_email': org_data.get('do_email'),
            'publisher_telephone_number': org_data.get('do_tel'),
            'publisher_country': org_data.get('country'),
            'publisher_administrative_area': org_data.get('administrative_area'),
            'publisher_postal_code': org_data.get('postal_code'),
            'publisher_city': org_data.get('city'),
            'publisher_street_address': org_data.get('street_address'),

            # Combine address components into a nested dictionary for complete address details
            'publisher_address': {
                'street_address': org_data.get('street_address'),
                'postal_code': org_data.get('postal_code'),
                'city': org_data.get('city'),
                'administrative_area': org_data.get('administrative_area'),
                'country': org_data.get('country')
            },

            # Combine publisher name components into a nested dictionary for complete publisher name details
            'publisher_name': {
                'publisher_firstname': pkg_dict.get(u'publisher_firstname'),
                'publisher_surname': pkg_dict.get(u'publisher_surname')
            }
        })

        return pkg_dict

    # IUploader
    def get_uploader(self, upload_to, old_filename):
        if upload_to == "group":
            return OrganizationUploader(upload_to, old_filename)
        return None

    def get_resource_uploader(self, data_dict):
        return None
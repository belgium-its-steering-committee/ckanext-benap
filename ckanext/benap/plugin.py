# coding=utf-8
from collections import OrderedDict

import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation
import json
from flask import Blueprint

from ckanext.benap.helpers import ontology_helper, scheming_language_text_fallback, json_loads, \
    package_notes_translated_fallback, field_translated_fallback, organisation_names_for_autocomplete, \
    get_translated_tags, scheming_language_text, format_datetime, ckan_tag_to_transport_mode_concept_label, \
    forum_url, filter_default_tags_only, getTranslatedVideoUrl, show_element, get_organization_by_id, benap_fluent_label, \
    translate_organization_filter, convert_validation_list_to_JSON, benap_get_organization_field_by_id, \
    benap_get_organization_field_by_specified_field, benap_retrieve_dict_items_or_keys_or_values, get_translated_category_and_sub_category, \
    benap_retrieve_org_title_tel_email, benap_retrieve_raw_choices_list, benap_tag_update_helper, _c, get_facet_label_function

from ckanext.benap.util.forms import map_for_form_select
from ckanext.benap.validators import phone_number_validator, \
    countries_covered_belgium, is_after_start, https_validator, modified_by_sysadmin, \
    is_choice_null, contact_point_org_fields_consistency_check, \
    license_fields_conditional_validation, benap_tag_string_convert, fluent_tags_validator, category_sub_category_validator
from ckanext.benap.helpers.concepts import get_concept_label

from ckanext.benap.logic.auth.get import user_autocomplete, user_list
from ckanext.benap.custom_group import CreateGroupView, EditGroupView

class BenapPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)
    plugins.implements(plugins.IValidators, inherit=True)
    plugins.implements(plugins.IAuthFunctions, inherit=False)
    plugins.implements(plugins.IFacets, inherit=True)
    plugins.implements(plugins.IPackageController, inherit=True)
    plugins.implements(plugins.IBlueprint, inherit=True)

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
        # toolkit.add_resource('fanstatic', 'nap_checked_pill_style.css')

    # ITemplateHelpers

    def get_helpers(self):
        return {
            '_c': _c,
            'benap_geographic_granularity_helper': lambda context: map_for_form_select(self.geographic_granularity_map),
            'benap_ontology_helper': ontology_helper,
            'benap_scheming_language_text_fallback': scheming_language_text_fallback,
            'benap_package_notes_translated_fallback': package_notes_translated_fallback,
            'benap_field_translated_fallback': field_translated_fallback,
            'json_loads': json_loads,
            'benap_organisation_names_for_autocomplete': organisation_names_for_autocomplete,
            'get_translated_tags': get_translated_tags,
            'ckan_tag_to_transport_mode_concept_label': ckan_tag_to_transport_mode_concept_label,
            'filter_default_tags_only': filter_default_tags_only,
            'benap_scheming_language_text': scheming_language_text,
            'format_datetime': format_datetime,
            'benap_forum_url': forum_url,
            'getTranslatedVideoUrl': getTranslatedVideoUrl,
            'benap_get_organization_by_id': get_organization_by_id,
            'translate_organization_filter': translate_organization_filter,
            'show_element': show_element,
            'benap_fluent_label': benap_fluent_label,
            'benap_convert_validation_list_to_JSON': convert_validation_list_to_JSON,
            'benap_get_organization_field_by_id': benap_get_organization_field_by_id,
            'benap_get_organization_field_by_specified_field': benap_get_organization_field_by_specified_field,
            'benap_retrieve_dict_items_or_keys_or_values': benap_retrieve_dict_items_or_keys_or_values,
            'benap_get_translated_category_and_sub_category': get_translated_category_and_sub_category,
            'benap_retrieve_org_title_tel_email': benap_retrieve_org_title_tel_email,
            'benap_retrieve_raw_choices_list': benap_retrieve_raw_choices_list,
            'benap_tag_update_helper': benap_tag_update_helper,
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
        }

    # IAuthFunctions

    def get_auth_functions(self):
        return {
            'user_list': user_list,
            'user_autocomplete': user_autocomplete,
        }

    # IFacets
    def dataset_facets(self, facets_dict, package_type):
        facets_dict = OrderedDict([
            ('nap_type', 'NAP Type'),
            #TODO make new mobility theme (old its_dataset_type) work in filters
            # (u'its_dataset_type', u'Dataset Type'),
            ('tags', 'Tags'),
            ('regions_covered_uri', 'Area covered by publication'),
            ('mobility_theme_uri', 'Mobility Theme'),
            ('organization', 'Organizations'),
            #TODO make new format and licenses fields work in filters
            # (u'res_format', u'Formats'),
            # (u'license_id', u'Licenses'),
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
    
        return blueprint

    # IPackageController
    def before_dataset_index(self, pkg_dict):
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

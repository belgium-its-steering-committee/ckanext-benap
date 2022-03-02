# coding=utf-8
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from ckan.lib.plugins import DefaultTranslation

from ckanext.benap.helpers import ontology_helper, scheming_language_text_fallback, json_loads, \
    package_notes_translated_fallback, field_translated_fallback, organisation_names_for_autocomplete,\
    get_translated_tags, scheming_language_text, format_datetime, get_translated_tag, get_translated_tag_with_name, \
    forum_url, filter_default_tags_only, getTranslatedVideoUrl, show_element, get_organization_by_id
from ckanext.benap.util.forms import map_for_form_select
from ckanext.benap.validators import phone_number_validator, countries_covered_belgium, is_after_start, https_validator
from ckanext.benap.logic.auth.get import user_list


class BenapPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm, DefaultTranslation):
    plugins.implements(plugins.ITranslation)
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)
    plugins.implements(plugins.IValidators, inherit=True)
    plugins.implements(plugins.IAuthFunctions, inherit=False)
    plugins.implements(plugins.IFacets, inherit=True)

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
            'get_organization_by_id': get_organization_by_id,
            'show_element': show_element
        }

    # IValidators

    def get_validators(self):
        return {
            'phone_number_validator': phone_number_validator,
            'benap_countries_covered_belgium': countries_covered_belgium,
            'benap_is_after_start': is_after_start,
            'benap_https_validator': https_validator
        }

    # IAuthFunctions

    def get_auth_functions(self):
        return {
            'user_list': user_list,
        }

    # IFacets
    def dataset_facets(self, facets_dict, package_type):
        facets_dict['regions_covered'] = plugins.toolkit._('Area covered by publication')
        print("#"*25)
        print(facets_dict)
        print("#"*25)
        return facets_dict


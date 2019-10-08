# coding=utf-8
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.benap.helpers import ontology_helper, scheming_language_text_fallback, json_loads, \
    package_notes_translated_fallback, field_translated_fallback, organisation_names_for_autocomplete,\
    get_translated_tags, scheming_language_text
from ckanext.benap.util.forms import map_for_form_select
from ckanext.benap.validators import phone_number_validator, countries_covered_belgium


class BenapPlugin(plugins.SingletonPlugin, toolkit.DefaultDatasetForm):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)
    plugins.implements(plugins.IValidators, inherit=True)

    geographic_granularity_map = [('', ''),
                                  ('national', 'National'),
                                  ('regional', 'Regional'),
                                  ('province', 'province-'),
                                  ('municipality', 'municipality'),
                                  ('other', 'other')]

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
            'get_translated_tags': get_translated_tags,
            'benap_scheming_language_text': scheming_language_text,
        }

    # IValidators

    def get_validators(self):
        return {
            'phone_number_validator': phone_number_validator,
            'benap_countries_covered_belgium': countries_covered_belgium
        }

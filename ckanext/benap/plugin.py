# coding=utf-8
import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit

from ckanext.benap.util.forms import map_for_form_select


class BenapPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer, inherit=True)
    plugins.implements(plugins.ITemplateHelpers, inherit=False)

    geographic_granularity_map = [('', ''),
                                  ('national', 'National'),
                                  ('regional', 'Regional'),
                                  ('province', 'province-'),
                                  ('municipality', 'municipality'),
                                  ('other', 'other')]

    def _ontology_helper(self, context):
        ontology = context.get("benap_helper_ontology", None)
        if ontology == "language":
            return map_for_form_select([
                ('http://publications.europa.eu/resource/authority/language/FRA', {
                    "en": "French",
                    "fr": "français",
                    "nl": "Frans",
                    "de": "Französisch"
                }),
                ('http://publications.europa.eu/resource/authority/language/ENG', {
                    "en": "English",
                    "fr": "anglais",
                    "nl": "Engels",
                    "de": "Englisch"
                }),
                ('http://publications.europa.eu/resource/authority/language/NLD', {
                    "en": "Dutch",
                    "fr": "néerlandais",
                    "nl": "Nederlands",
                    "de": "Niederländisch"
                }),
                ('http://publications.europa.eu/resource/authority/language/DEU', {
                    "en": "German",
                    "fr": "allemand",
                    "nl": "Duits",
                    "de": "Deutsch"
                }),
            ])
        elif ontology == "data-theme":
            return map_for_form_select([
                ('http://publications.europa.eu/resource/authority/data-theme/TRAN', {
                    "en": "Transport",
                    "fr": "Transports",
                    "nl": "Vervoer",
                    "de": "Verkehr"
                })
            ])
        elif ontology == "frequency":
            return map_for_form_select([
                ('http://publications.europa.eu/resource/authority/frequency/NEVER', {
                    "en": "Never"
                }),
                ('http://publications.europa.eu/resource/authority/frequency/ANNUAL', {
                    "en": "Annual"
                }),
                ('http://publications.europa.eu/resource/authority/frequency/MONTHLY', {
                    "en": "Monthly"
                }),
                ('http://publications.europa.eu/resource/authority/frequency/WEEKLY', {
                    "en": "Weekly"
                })
            ])
        return None

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('fanstatic', 'benap')

    # ITemplateHelpers

    def get_helpers(self):
        return {
            'benap_geographic_granularity_helper': lambda context: map_for_form_select(self.geographic_granularity_map),
            'benap_ontology_helper': self._ontology_helper
        }

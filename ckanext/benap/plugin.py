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
                    "fr": "Français",
                    "nl": "Frans",
                    "de": "Französisch"
                }),
                ('http://publications.europa.eu/resource/authority/language/NLD', {
                    "en": "Dutch",
                    "fr": "Néerlandais",
                    "nl": "Nederlands",
                    "de": "Niederländisch"
                }),
                ('http://publications.europa.eu/resource/authority/language/DEU', {
                    "en": "German",
                    "fr": "Allemand",
                    "nl": "Duits",
                    "de": "Deutsch"
                }),
                ('http://publications.europa.eu/resource/authority/language/ENG', {
                    "en": "English",
                    "fr": "Anglais",
                    "nl": "Engels",
                    "de": "Englisch"
                }),
            ])
            if ontology == "EU-language":
                return map_for_form_select([
                    ('http://publications.europa.eu/resource/authority/language/BUL', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/HRV', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/CES', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/DAN', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/NLD', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/ENG', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/EST', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/FIN', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/FRA', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/DEU', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/ELL', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/HUN', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/GLE', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/ITA', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/LAV', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/LIT', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/MLT', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/POL', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/POR', {
                        "en": "French",
                        "fr": "Français",
                        "nl": "Frans",
                        "de": "Französisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/RON', {
                        "en": "Dutch",
                        "fr": "Néerlandais",
                        "nl": "Nederlands",
                        "de": "Niederländisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/SLK', {
                        "en": "German",
                        "fr": "Allemand",
                        "nl": "Duits",
                        "de": "Deutsch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/SLV', {
                        "en": "English",
                        "fr": "Anglais",
                        "nl": "Engels",
                        "de": "Englisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/SPA', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
                    }),
                    ('http://publications.europa.eu/resource/authority/language/SWE', {
                        "en": "",
                        "fr": "",
                        "nl": "",
                        "de": ""
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

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
                    "en": u"French",
                    "fr": u"Français",
                    "nl": u"Frans",
                    "de": u"Französisch"
                }),
                ('http://publications.europa.eu/resource/authority/language/ENG', {
                    "en": u"English",
                    "fr": u"Anglais",
                    "nl": u"Engels",
                    "de": u"Englisch"
                }),
                ('http://publications.europa.eu/resource/authority/language/NLD', {
                    "en": u"Dutch",
                    "fr": u"Néerlandais",
                    "nl": u"Nederlands",
                    "de": u"Niederländisch"
                }),
                ('http://publications.europa.eu/resource/authority/language/DEU', {
                    "en": u"German",
                    "fr": u"Allemand",
                    "nl": u"Duits",
                    "de": u"Deutsch"
                }),
            ])

        if ontology == "EU-language":
            return map_for_form_select([
                ('http://publications.europa.eu/resource/authority/language/BUL', {
                    "en": u"Bulgarian",
                    "fr": u"Bulgare",
                    "nl": u"Bulgaars",
                    "de": u"Bulgarisch"
                }),
                    ('http://publications.europa.eu/resource/authority/language/HRV', {
                        "en": u"Croatian",
                        "fr": u"Croate",
                        "nl": u"Kroatisch",
                        "de": u"Kroatisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/CES', {
                        "en": u"Czech",
                        "fr": u"Tchèque",
                        "nl": u"Tsjechisch",
                        "de": u"Tschechisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/DAN', {
                        "en": u"Danish",
                        "fr": u"Danois",
                        "nl": u"Deens",
                        "de": u"Dänisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/NLD', {
                        "en": u"Dutch",
                        "fr": u"Néerlandais",
                        "nl": u"Nederlands",
                        "de": u"Niederländisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/ENG', {
                        "en": u"English",
                        "fr": u"Anglais",
                        "nl": u"Engels",
                        "de": u"Englisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/EST', {
                        "en": u"Estonian",
                        "fr": u"Estonien",
                        "nl": u"Ests",
                        "de": u"Estnisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/FIN', {
                        "en": u"Finnish",
                        "fr": u"Finnois",
                        "nl": u"Fins",
                        "de": u"Finnisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/FRA', {
                        "en": u"French",
                        "fr": u"Français",
                        "nl": u"Frans",
                        "de": u"Französisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/DEU', {
                        "en": u"German",
                        "fr": u"Allemand",
                        "nl": u"Duits",
                        "de": u"Deutsch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/ELL', {
                        "en": u"Greek",
                        "fr": u"Grec",
                        "nl": u"Grieks",
                        "de": u"Griechisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/HUN', {
                        "en": u"Hungarian",
                        "fr": u"Hongrois",
                        "nl": u"Hongaars",
                        "de": u"Ungarisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/GLE', {
                        "en": u"Irish",
                        "fr": u"Irlandais",
                        "nl": u"Iers",
                        "de": u"Irisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/ITA', {
                        "en": u"Italian",
                        "fr": u"Italien",
                        "nl": u"Italiaans",
                        "de": u"Italienisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/LAV', {
                        "en": u"Latvian",
                        "fr": u"Letton",
                        "nl": u"Lets",
                        "de": u"Lettisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/LIT', {
                        "en": u"Lithuanian",
                        "fr": u"Lituanien",
                        "nl": u"Litouws",
                        "de": u"Litauisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/MLT', {
                        "en": u"Maltese",
                        "fr": u"Maltais",
                        "nl": u"Maltees",
                        "de": u"Maltesisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/POL', {
                        "en": u"Polish",
                        "fr": u"Polonais",
                        "nl": u"Pools",
                        "de": u"Polnisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/POR', {
                        "en": u"Portuguese",
                        "fr": u"Portugais",
                        "nl": u"Portugees",
                        "de": u"Portugiesisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/RON', {
                        "en": u"Romanian",
                        "fr": u"Roumain",
                        "nl": u"Roemeens",
                        "de": u"Rumänisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/SLK', {
                        "en": u"Slovak",
                        "fr": u"Slovaque",
                        "nl": u"Slowaaks",
                        "de": u"Slowakisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/SLV', {
                        "en": u"Slovenian",
                        "fr": u"Slovène",
                        "nl": u"Sloveens",
                        "de": u"Slowenisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/SPA', {
                        "en": u"Spanish",
                        "fr": u"Espagnol",
                        "nl": u"Spaans",
                        "de": u"Spanisch"
                    }),
                    ('http://publications.europa.eu/resource/authority/language/SWE', {
                        "en": u"Swedish",
                        "fr": u"Suédois",
                        "nl": u"Zweeds",
                        "de": u"Schwedisch"
                    }),
            ])



        elif ontology == "data-theme":
            return map_for_form_select([
                ('http://publications.europa.eu/resource/authority/data-theme/TRAN', {
                    "en": u"Transport",
                    "fr": u"Transports",
                    "nl": u"Vervoer",
                    "de": u"Verkehr"
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

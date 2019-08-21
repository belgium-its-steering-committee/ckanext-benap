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
        if ontology == "NUTS3_BE":
            return map_for_form_select([
                ('http://data.europa.eu/nuts/code/BE100', {
                    "en": u"Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad",
                    "fr": u"Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad",
                    "nl": u"Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad",
                    "de": u"Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad"
                }),
                    ('http://data.europa.eu/nuts/code/BE211', {
                        "en": u"Arr. Antwerpen",
                        "fr": u"Arr. Antwerpen",
                        "nl": u"Arr. Antwerpen",
                        "de": u"Arr. Antwerpen"
                    }),
                    ('http://data.europa.eu/nuts/code/BE212', {
                        "en": u"Arr. Mechelen",
                        "fr": u"Arr. Mechelen",
                        "nl": u"Arr. Mechelen",
                        "de": u"Arr. Mechelen"
                    }),
                    ('http://data.europa.eu/nuts/code/BE213', {
                        "en": u"Arr. Turnhout",
                        "fr": u"Arr. Turnhout",
                        "nl": u"Arr. Turnhout",
                        "de": u"Arr. Turnhout"
                    }),
                    ('http://data.europa.eu/nuts/code/BE221', {
                        "en": u"Arr. Hasselt",
                        "fr": u"Arr. Hasselt",
                        "nl": u"Arr. Hasselt",
                        "de": u"Arr. Hasselt"
                    }),
                    ('http://data.europa.eu/nuts/code/BE222', {
                        "en": u"Arr. Maaseik",
                        "fr": u"Arr. Maaseik",
                        "nl": u"Arr. Maaseik",
                        "de": u"Arr. Maaseik"
                    }),
                    ('http://data.europa.eu/nuts/code/BE223', {
                        "en": u"Arr. Tongeren",
                        "fr": u"Arr. Tongeren",
                        "nl": u"Arr. Tongeren",
                        "de": u"Arr. Tongeren"
                    }),
                    ('http://data.europa.eu/nuts/code/BE231', {
                        "en": u"Arr. Aalst",
                        "fr": u"Arr. Aalst",
                        "nl": u"Arr. Aalst",
                        "de": u"Arr. Aalst"
                    }),
                    ('http://data.europa.eu/nuts/code/BE232', {
                        "en": u"Arr. Dendermonde",
                        "fr": u"Arr. Dendermonde",
                        "nl": u"Arr. Dendermonde",
                        "de": u"Arr. Dendermonde"
                    }),
                    ('http://data.europa.eu/nuts/code/BE233', {
                        "en": u"Arr. Eeklo",
                        "fr": u"Arr. Eeklo",
                        "nl": u"Arr. Eeklo",
                        "de": u"Arr. Eeklo"
                    }),
                    ('http://data.europa.eu/nuts/code/BE234', {
                        "en": u"Arr. Gent",
                        "fr": u"Arr. Gent",
                        "nl": u"Arr. Gent",
                        "de": u"Arr. Gent"
                    }),
                    ('http://data.europa.eu/nuts/code/BE235', {
                        "en": u"Arr. Oudenaarde",
                        "fr": u"Arr. Oudenaarde",
                        "nl": u"Arr. Oudenaarde",
                        "de": u"Arr. Oudenaarde"
                    }),
                    ('http://data.europa.eu/nuts/code/BE236', {
                        "en": u"Arr. Sint-Niklaas",
                        "fr": u"Arr. Sint-Niklaas",
                        "nl": u"Arr. Sint-Niklaas",
                        "de": u"Arr. Sint-Niklaas"
                    }),
                    ('http://data.europa.eu/nuts/code/BE241', {
                        "en": u"Arr. Halle-Vilvoorde",
                        "fr": u"Arr. Halle-Vilvoorde",
                        "nl": u"Arr. Halle-Vilvoorde",
                        "de": u"Arr. Halle-Vilvoorde"
                    }),
                    ('http://data.europa.eu/nuts/code/BE242', {
                        "en": u"Arr. Leuven",
                        "fr": u"Arr. Leuven",
                        "nl": u"Arr. Leuven",
                        "de": u"Arr. Leuven"
                    }),
                    ('http://data.europa.eu/nuts/code/BE251', {
                        "en": u"Arr. Brugge",
                        "fr": u"Arr. Brugge",
                        "nl": u"Arr. Brugge",
                        "de": u"Arr. Brugge"
                    }),
                    ('http://data.europa.eu/nuts/code/BE252', {
                        "en": u"Arr. Diksmuide",
                        "fr": u"Arr. Diksmuide",
                        "nl": u"Arr. Diksmuide",
                        "de": u"Arr. Diksmuide"
                    }),
                    ('http://data.europa.eu/nuts/code/BE253', {
                        "en": u"Arr. Ieper",
                        "fr": u"Arr. Ieper",
                        "nl": u"Arr. Ieper",
                        "de": u"Arr. Ieper"
                    }),
                    ('http://data.europa.eu/nuts/code/BE254', {
                        "en": u"Arr. Kortrijk",
                        "fr": u"Arr. Kortrijk",
                        "nl": u"Arr. Kortrijk",
                        "de": u"Arr. Kortrijk"
                    }),
                    ('http://data.europa.eu/nuts/code/BE255', {
                        "en": u"Arr. Oostende",
                        "fr": u"Arr. Oostende",
                        "nl": u"Arr. Oostende",
                        "de": u"Arr. Oostende"
                    }),
                    ('http://data.europa.eu/nuts/code/BE256', {
                        "en": u"Arr. Roeselare",
                        "fr": u"Arr. Roeselare",
                        "nl": u"Arr. Roeselare",
                        "de": u"Arr. Roeselare"
                    }),
                    ('http://data.europa.eu/nuts/code/BE257', {
                        "en": u"Arr. Tielt",
                        "fr": u"Arr. Tielt",
                        "nl": u"Arr. Tielt",
                        "de": u"Arr. Tielt"
                    }),
                    ('http://data.europa.eu/nuts/code/BE258', {
                        "en": u"Arr. Veurne",
                        "fr": u"Arr. Veurne",
                        "nl": u"Arr. Veurne",
                        "de": u"Arr. Veurne"
                    }),
                    ('http://data.europa.eu/nuts/code/BE310', {
                        "en": u"Arr. Nivelles",
                        "fr": u"Arr. Nivelles",
                        "nl": u"Arr. Nivelles",
                        "de": u"Arr. Nivelles"
                    }),
                    ('http://data.europa.eu/nuts/code/321', {
                        "en": u"Arr. Ath",
                        "fr": u"Arr. Ath",
                        "nl": u"Arr. Ath",
                        "de": u"Arr. Ath"
                    }),
                    ('http://data.europa.eu/nuts/code/322', {
                        "en": u"Arr. Charleroi",
                        "fr": u"Arr. Charleroi",
                        "nl": u"Arr. Charleroi",
                        "de": u"Arr. Charleroi"
                    }),
                    ('http://data.europa.eu/nuts/code/323', {
                        "en": u"Arr. Mons",
                        "fr": u"Arr. Mons",
                        "nl": u"Arr. Mons",
                        "de": u"Arr. Mons"
                    }),
                    ('http://data.europa.eu/nuts/code/', {
                        "en": u"Arr. Mouscron",
                        "fr": u"Arr. Mouscron",
                        "nl": u"Arr. Mouscron",
                        "de": u"Arr. Mouscron"
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

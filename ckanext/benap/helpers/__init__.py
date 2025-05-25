# coding=utf-8
import json
import ckan.plugins.toolkit as toolkit
from ckan.common import config
import logging
from .decorators import decorator_timer
from itertools import chain

from ckanext.benap.helpers.lists import (NUTS1_BE, GEOREFERENCING_METHOD, DATASET_TYPE, NAP_TYPE, NETWORK_COVERAGE,
                                         MOBILITY_THEME, CONDITIONS_USAGE, CONDITIONS_ACCESS, LICENSE_TYPE, FREQUENCY,
                                         REFERENCE_SYSTEM, DATA_MODEL, SYNTAX, APPLICATION_LAYER_PROTOCOL, COMMUNICATION_METHOD, 
                                         GRAMMAR, ENCODING)

from ckanext.benap.util.forms import map_for_form_select
from ckanext.scheming.helpers import scheming_get_dataset_schema

log = logging.getLogger(__name__)

def user_language():
    try:
        from ckantoolkit import h
        return h.lang()
    except TypeError:
        return None  # lang() call will fail when no user language available


def ontology_helper(context):
    ontology = context.get("benap_helper_ontology", None)
    if ontology == "language":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/language/FRA', {
                "en": "French",
                "fr": "Français",
                "nl": "Frans",
                "de": "Französisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/ENG', {
                "en": "English",
                "fr": "Anglais",
                "nl": "Engels",
                "de": "Englisch"
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
        ])

    elif ontology == "EU_COUNTRY":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/country/BEL', {
                "en": "Belgium",
                "fr": "Belgique",
                "nl": "België",
                "de": "Belgien"
            }),
            ('http://publications.europa.eu/resource/authority/country/NLD', {
                "en": "Netherlands",
                "fr": "Pays-Bas",
                "nl": "Nederland",
                "de": "Niederlande"
            }),
            ('http://publications.europa.eu/resource/authority/country/FRA', {
                "en": "France",
                "fr": "France",
                "nl": "Frankrijk",
                "de": "Frankreich"
            }),
            ('http://publications.europa.eu/resource/authority/country/DEU', {
                "en": "Germany",
                "fr": "Allemagne",
                "nl": "Duitsland",
                "de": "Deutschland"
            }),
            ('http://publications.europa.eu/resource/authority/country/LUX', {
                "en": "Luxembourg",
                "fr": "Luxembourg",
                "nl": "Luxemburg",
                "de": "Luxemburg"
            }),
            ('http://publications.europa.eu/resource/authority/country/GBR', {
                "en": "United Kingdom",
                "fr": "Royaume-Uni",
                "nl": "Verenigd Koninkrijk",
                "de": "Vereinigtes Königreich"
            }),
            ('http://publications.europa.eu/resource/authority/country/BGR', {
                "en": "Bulgaria",
                "fr": "Bulgarie",
                "nl": "Bulgarije",
                "de": "Bulgarien"
            }),
            ('http://publications.europa.eu/resource/authority/country/CZE', {
                "en": "Czechia",
                "fr": "Tchéquie",
                "nl": "Tsjechië",
                "de": "Tschechien"
            }),
            ('http://publications.europa.eu/resource/authority/country/DNK', {
                "en": "Denmark",
                "fr": "Danemark",
                "nl": "Denemarken",
                "de": "Dänemark"
            }),
            ('http://publications.europa.eu/resource/authority/country/EST', {
                "en": "Estonia",
                "fr": "Estonie",
                "nl": "Estland",
                "de": "Estland"
            }),
            ('http://publications.europa.eu/resource/authority/country/IRL', {
                "en": "Ireland",
                "fr": "Irlande",
                "nl": "Ierland",
                "de": "Irland"
            }),
            ('http://publications.europa.eu/resource/authority/country/GRC', {
                "en": "Greece",
                "fr": "Grèce",
                "nl": "Griekenland",
                "de": "Griechenland"
            }),
            ('http://publications.europa.eu/resource/authority/country/ESP', {
                "en": "Spain",
                "fr": "Espagne",
                "nl": "Spanje",
                "de": "Spanien"
            }),
            ('http://publications.europa.eu/resource/authority/country/HRV', {
                "en": "Croatia",
                "fr": "Croatie",
                "nl": "Kroatië",
                "de": "Kroatien"
            }),
            ('http://publications.europa.eu/resource/authority/country/ITA', {
                "en": "Italy",
                "fr": "Italie",
                "nl": "Italië",
                "de": "Italien"
            }),
            ('http://publications.europa.eu/resource/authority/country/CYP', {
                "en": "Cyprus",
                "fr": "Chypre",
                "nl": "Cyprus",
                "de": "Zypern"
            }),
            ('http://publications.europa.eu/resource/authority/country/LVA', {
                "en": "Latvia",
                "fr": "Lettonie",
                "nl": "Letland",
                "de": "Lettland"
            }),
            ('http://publications.europa.eu/resource/authority/country/LTU', {
                "en": "Lithuania",
                "fr": "Lituanie",
                "nl": "Litouwen",
                "de": "Litauen"
            }),
            ('http://publications.europa.eu/resource/authority/country/HUN', {
                "en": "Hungary",
                "fr": "Hongrie",
                "nl": "Hongarije",
                "de": "Ungarn"
            }),
            ('http://publications.europa.eu/resource/authority/country/MLT', {
                "en": "Malta",
                "fr": "Malte",
                "nl": "Malta",
                "de": "Malta"
            }),
            ('http://publications.europa.eu/resource/authority/country/AUT', {
                "en": "Austria",
                "fr": "Autriche",
                "nl": "Oostenrijk",
                "de": "Österreich"
            }),
            ('http://publications.europa.eu/resource/authority/country/POL', {
                "en": "Poland",
                "fr": "Pologne",
                "nl": "Polen",
                "de": "Polen"
            }),
            ('http://publications.europa.eu/resource/authority/country/PRT', {
                "en": "Portugal",
                "fr": "Portugal",
                "nl": "Portugal",
                "de": "Portugal"
            }),
            ('http://publications.europa.eu/resource/authority/country/ROU', {
                "en": "Romania",
                "fr": "Roumanie",
                "nl": "Roemenië",
                "de": "Rumänien"
            }),
            ('http://publications.europa.eu/resource/authority/country/SVN', {
                "en": "Slovenia",
                "fr": "Slovénie",
                "nl": "Slovenië",
                "de": "Slowenien"
            }),
            ('http://publications.europa.eu/resource/authority/country/SVK', {
                "en": "Slovakia",
                "fr": "Slovaquie",
                "nl": "Slowakije",
                "de": "Slowakei"
            }),
            ('http://publications.europa.eu/resource/authority/country/FIN', {
                "en": "Finland",
                "fr": "Finlande",
                "nl": "Finland",
                "de": "Finnland"
            }),
            ('http://publications.europa.eu/resource/authority/country/SWE', {
                "en": "Sweden",
                "fr": "Suède",
                "nl": "Zweden",
                "de": "Schweden"
            }),
        ])
    elif ontology == "NUTS1_BE":
        return map_for_form_select(NUTS1_BE)
    elif ontology == "NUTS3_BE":
        return map_for_form_select([
            ('http://data.europa.eu/nuts/code/BE100', {
                "en": "Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad",
                "fr": "Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad",
                "nl": "Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad",
                "de": "Arr. de Bruxelles-Capitale / Arr. van Brussel-Hoofdstad"
            }),
            ('http://data.europa.eu/nuts/code/BE211', {
                "en": "Arr. Antwerpen",
                "fr": "Arr. Antwerpen",
                "nl": "Arr. Antwerpen",
                "de": "Arr. Antwerpen"
            }),
            ('http://data.europa.eu/nuts/code/BE212', {
                "en": "Arr. Mechelen",
                "fr": "Arr. Mechelen",
                "nl": "Arr. Mechelen",
                "de": "Arr. Mechelen"
            }),
            ('http://data.europa.eu/nuts/code/BE213', {
                "en": "Arr. Turnhout",
                "fr": "Arr. Turnhout",
                "nl": "Arr. Turnhout",
                "de": "Arr. Turnhout"
            }),
            ('http://data.europa.eu/nuts/code/BE221', {
                "en": "Arr. Hasselt",
                "fr": "Arr. Hasselt",
                "nl": "Arr. Hasselt",
                "de": "Arr. Hasselt"
            }),
            ('http://data.europa.eu/nuts/code/BE222', {
                "en": "Arr. Maaseik",
                "fr": "Arr. Maaseik",
                "nl": "Arr. Maaseik",
                "de": "Arr. Maaseik"
            }),
            ('http://data.europa.eu/nuts/code/BE223', {
                "en": "Arr. Tongeren",
                "fr": "Arr. Tongeren",
                "nl": "Arr. Tongeren",
                "de": "Arr. Tongeren"
            }),
            ('http://data.europa.eu/nuts/code/BE231', {
                "en": "Arr. Aalst",
                "fr": "Arr. Aalst",
                "nl": "Arr. Aalst",
                "de": "Arr. Aalst"
            }),
            ('http://data.europa.eu/nuts/code/BE232', {
                "en": "Arr. Dendermonde",
                "fr": "Arr. Dendermonde",
                "nl": "Arr. Dendermonde",
                "de": "Arr. Dendermonde"
            }),
            ('http://data.europa.eu/nuts/code/BE233', {
                "en": "Arr. Eeklo",
                "fr": "Arr. Eeklo",
                "nl": "Arr. Eeklo",
                "de": "Arr. Eeklo"
            }),
            ('http://data.europa.eu/nuts/code/BE234', {
                "en": "Arr. Gent",
                "fr": "Arr. Gent",
                "nl": "Arr. Gent",
                "de": "Arr. Gent"
            }),
            ('http://data.europa.eu/nuts/code/BE235', {
                "en": "Arr. Oudenaarde",
                "fr": "Arr. Oudenaarde",
                "nl": "Arr. Oudenaarde",
                "de": "Arr. Oudenaarde"
            }),
            ('http://data.europa.eu/nuts/code/BE236', {
                "en": "Arr. Sint-Niklaas",
                "fr": "Arr. Sint-Niklaas",
                "nl": "Arr. Sint-Niklaas",
                "de": "Arr. Sint-Niklaas"
            }),
            ('http://data.europa.eu/nuts/code/BE241', {
                "en": "Arr. Halle-Vilvoorde",
                "fr": "Arr. Halle-Vilvoorde",
                "nl": "Arr. Halle-Vilvoorde",
                "de": "Arr. Halle-Vilvoorde"
            }),
            ('http://data.europa.eu/nuts/code/BE242', {
                "en": "Arr. Leuven",
                "fr": "Arr. Leuven",
                "nl": "Arr. Leuven",
                "de": "Arr. Leuven"
            }),
            ('http://data.europa.eu/nuts/code/BE251', {
                "en": "Arr. Brugge",
                "fr": "Arr. Brugge",
                "nl": "Arr. Brugge",
                "de": "Arr. Brugge"
            }),
            ('http://data.europa.eu/nuts/code/BE252', {
                "en": "Arr. Diksmuide",
                "fr": "Arr. Diksmuide",
                "nl": "Arr. Diksmuide",
                "de": "Arr. Diksmuide"
            }),
            ('http://data.europa.eu/nuts/code/BE253', {
                "en": "Arr. Ieper",
                "fr": "Arr. Ieper",
                "nl": "Arr. Ieper",
                "de": "Arr. Ieper"
            }),
            ('http://data.europa.eu/nuts/code/BE254', {
                "en": "Arr. Kortrijk",
                "fr": "Arr. Kortrijk",
                "nl": "Arr. Kortrijk",
                "de": "Arr. Kortrijk"
            }),
            ('http://data.europa.eu/nuts/code/BE255', {
                "en": "Arr. Oostende",
                "fr": "Arr. Oostende",
                "nl": "Arr. Oostende",
                "de": "Arr. Oostende"
            }),
            ('http://data.europa.eu/nuts/code/BE256', {
                "en": "Arr. Roeselare",
                "fr": "Arr. Roeselare",
                "nl": "Arr. Roeselare",
                "de": "Arr. Roeselare"
            }),
            ('http://data.europa.eu/nuts/code/BE257', {
                "en": "Arr. Tielt",
                "fr": "Arr. Tielt",
                "nl": "Arr. Tielt",
                "de": "Arr. Tielt"
            }),
            ('http://data.europa.eu/nuts/code/BE258', {
                "en": "Arr. Veurne",
                "fr": "Arr. Veurne",
                "nl": "Arr. Veurne",
                "de": "Arr. Veurne"
            }),
            ('http://data.europa.eu/nuts/code/BE310', {
                "en": "Arr. Nivelles",
                "fr": "Arr. Nivelles",
                "nl": "Arr. Nivelles",
                "de": "Arr. Nivelles"
            }),
            ('http://data.europa.eu/nuts/code/BE321', {
                "en": "Arr. Ath",
                "fr": "Arr. Ath",
                "nl": "Arr. Ath",
                "de": "Arr. Ath"
            }),
            ('http://data.europa.eu/nuts/code/BE322', {
                "en": "Arr. Charleroi",
                "fr": "Arr. Charleroi",
                "nl": "Arr. Charleroi",
                "de": "Arr. Charleroi"
            }),
            ('http://data.europa.eu/nuts/code/BE323', {
                "en": "Arr. Mons",
                "fr": "Arr. Mons",
                "nl": "Arr. Mons",
                "de": "Arr. Mons"
            }),
            ('http://data.europa.eu/nuts/code/BE324', {
                "en": "Arr. Mouscron",
                "fr": "Arr. Mouscron",
                "nl": "Arr. Mouscron",
                "de": "Arr. Mouscron"
            }),
        ])

    elif ontology == "encoding":
        return map_for_form_select(ENCODING)

    elif ontology == "syntax":
        return map_for_form_select(SYNTAX)

    elif ontology == "grammar":
        return map_for_form_select(GRAMMAR)

    elif ontology == "datamodel":
        return map_for_form_select(DATA_MODEL)

    elif ontology == "protocol":
        return map_for_form_select(APPLICATION_LAYER_PROTOCOL)

    elif ontology == "communication":
        return map_for_form_select(COMMUNICATION_METHOD)

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
        return map_for_form_select(FREQUENCY)
    elif ontology == "georeferencing_method":
        return map_for_form_select(GEOREFERENCING_METHOD)
    elif ontology == "dataset_type":
        return map_for_form_select(DATASET_TYPE)
    elif ontology == "nap_type":
        return map_for_form_select(NAP_TYPE)
    elif ontology == "network_coverage":
        return map_for_form_select(NETWORK_COVERAGE)
    elif ontology =="mobility_theme":
        values_labels_list = [item for sublist in get_translated_category_and_sub_category() for tuples in sublist for item in tuples]
        return map_for_form_select(values_labels_list)
    elif ontology == "conditions_access":
        return map_for_form_select(CONDITIONS_ACCESS)
    elif ontology == "conditions_usage":
        return map_for_form_select(CONDITIONS_USAGE)
    elif ontology == "license_type":
        return map_for_form_select(LICENSE_TYPE)
    elif ontology == "reference_system":
        return map_for_form_select(REFERENCE_SYSTEM)
    return None


# TODO: This translation should be done using the plugin translation mechanism
# It should be done in the IFacets implementation of this plugin
def translate_organization_filter(facet_title, lang):
    if facet_title == "Organizations":
        return {
            "en": "Organizations", 
            "nl": "Organisaties", 
            "fr": "Organisations", 
            "de": "Organisationen"}[lang]
    elif facet_title == "NAP Type":
        return {
            "en": "NAP type", 
            "nl": "NAP type", 
            "fr": "Type de NAP", 
            "de": "NAP typ"}[lang]
    return facet_title



def scheming_language_text_fallback(field_data, language_data):
    return field_data['en'] or field_data['nl'] or field_data['fr'] or field_data['de']


def package_notes_translated_fallback(package):
    notes_value = None
    user_lang = user_language()
    notes_translated = package.get('notes_translated', None)
    if notes_translated:
        if user_lang:
            notes_value = notes_translated.get(user_lang, None)
        if not notes_value:
            notes_value = notes_translated['en'] or notes_translated['nl'] or notes_translated['fr'] \
                          or notes_translated['de'] or None
    return notes_value


def field_translated_fallback(translated_field):
    field_value = None
    user_lang = user_language()
    if translated_field:
        if user_lang:
            field_value = translated_field.get(user_lang, None)
        if not field_value:
            field_value = translated_field['en'] or translated_field['nl'] or translated_field['fr'] \
                          or translated_field['de'] or None
    return field_value


def json_loads(data):
    return json.dumps(json.loads(data))


def forum_url():
    return config.get('ckan.pages.forum.link', '')


def organisation_names_for_autocomplete():
    from ckantoolkit import h
    return [org['title'] for org in h.organizations_available('create_dataset')]


def format_datetime(datetime):
    return datetime.replace('T', ' ')[:-7]


def scheming_language_text(field_data, language_data):
    return field_data[language_data]


def get_translated_tag_with_name(tagName, lang):
    return get_translated_tag(dict([(key, tagName) for key in {'name'}]), lang)


def get_translated_tag(tag, lang):
    tags = get_translated_tags()
    tags.append(tuple([NUTS1_BE]))
    tags.append(tuple([DATASET_TYPE]))
    tags.append(tuple([NAP_TYPE]))
    try:

        return [x for x in [translated_tag for translated_taglist in
                                                      [categorized_tags[0] for categorized_tags in
                                                       tags] for translated_tag in
                                                      translated_taglist] if x[0] == benap_tag_mapping(tag['name'])][0][1][lang]
    except:
        try:
            return tag['display_name']
        except KeyError:
            try:
                if isinstance(tag, str):
                    return tag
                print(('tag not found: ' + json.dumps(tag)))
            except:
                print('tag not found')


def get_translated_tags():
    return [
        ([
            ("https://w3id.org/mobilitydcat-ap/transport-mode/air",
             {
                 "en": "Air",
                 "fr": "Aérien",
                 "nl": "Vliegtuig",
                 "de": "Luftverkehr"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/long-distance-rail",
             {
                 "en": "Rail (including high speed rail)",
                 "fr": "Ferroviaire (y compris ferroviaire à grande vitesse)",
                 "nl": "Trein (m.i.v. hogesnelheidstrein)",
                 "de": "Eisenbahn (einschl. Hochgeschwindigkeit)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/regional-and-local-rail",
             {
                 "en": "Conventional rail",
                 "fr": "Ferroviaire conventionnel",
                 "nl": "Klassieke trein",
                 "de": "Konventioneller Bahnverkehr"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/long-distance-coach",
             {
                 "en": "Long-distance coach",
                 "fr": "Autocar longue distance",
                 "nl": "Langeafstandsbus",
                 "de": "Fernbus"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/maritime",
             {
                 "en": "Maritime (including ferry)",
                 "fr": "Maritime (y compris les ferries)",
                 "nl": "Schip (m.i.v. veerboten)",
                 "de": "Schifffahrt (einschließlich Fähre)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/metro-subway-train",
             {
                 "en": "Metro",
                 "fr": "Métro",
                 "nl": "Metro",
                 "de": "Untergrundbahn"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/tram-light-rail",
             {
                 "en": "Tram, Light rail",
                 "fr": "Tram, Ferroviaire léger",
                 "nl": "Tram, Light rail",
                 "de": "Straßenbahn, Stadtbahn"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/bus",
             {
                 "en": "Bus",
                 "fr": "Bus",
                 "nl": "Bus",
                 "de": "Bus"
             })
        ], {
             "en": "Scheduled",
             "nl": "Openbaar vervoer",
             "fr": "Services réguliers",
             "de": "Linienverkehrsdienste"
         }),
        ([
            ("https://w3id.org/mobilitydcat-ap/transport-mode/shuttle-bus",
             {
                 "en": "Shuttle bus",
                 "fr": "Bus",
                 "nl": "Shuttlebus",
                 "de": "Pendelbus"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/shuttle-ferry",
             {
                 "en": "Shuttle ferry",
                 "fr": "Ferry",
                 "nl": "Shuttleveerboot",
                 "de": "Pendelfähre"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/taxi",
             {
                 "en": "Taxi",
                 "fr": "Taxi",
                 "nl": "Taxi",
                 "de": "Taxi"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/car-sharing",
             {
                 "en": "Car-sharing",
                 "fr": "Voitures partagées",
                 "nl": "Deelauto",
                 "de": "Gemeinsame Pkw-Nutzung (Car-Sharing)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/car-pooling",
             {
                 "en": "Car-pooling",
                 "fr": "Covoiturage",
                 "nl": "Carpooling",
                 "de": "Fahrgemeinschaften (Car-Pooling)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/car-hire",
             {
                 "en": "Car-hire",
                 "fr": "Location de voitures",
                 "nl": "Huurauto",
                 "de": "Mietwagen"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/bike-sharing",
             {
                 "en": "Bike-sharing",
                 "fr": "Vélos partagés",
                 "nl": "Deelfiets",
                 "de": "Gemeinsame Nutzung von Fahrrädern (Bike-Sharing)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/bike-hire",
             {
                 "en": "Bike-hire",
                 "fr": "Vélos en libre service",
                 "nl": "Huurfiets",
                 "de": "Leihfahrrad"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/ride-pooling",
             {
                 "en": "Ride-pooling",
                 "fr": "Trajets partagés",
                 "nl": "Gedeelde ritten",
                 "de": "Mitfahrdienst"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/e-scooter",
             {
                 "en": "E-scooter",
                 "fr": "Trottinettes électriques",
                 "nl": "E-scooter",
                 "de": "E-rollern"
             })
        ], {
             "en": "Demand-responsive",
             "nl": "Aanbod afhankelijke inzet",
             "fr": "Services à la demande",
             "de": "Abruf-Verkehrsdienste"
         }),
        ([
            ("https://w3id.org/mobilitydcat-ap/transport-mode/car",
             {
                 "en": "Car",
                 "fr": "Voiture",
                 "nl": "Auto",
                 "de": "Pkw"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/truck",
             {
                 "en": "Truck",
                 "fr": "Camion",
                 "nl": "Vrachtwagen",
                 "de": "Lastwagen"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/motorcycle",
             {
                 "en": "Motorcycle",
                 "fr": "Moto",
                 "nl": "Motorfiets",
                 "de": "Motorrad"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/bicycle",
             {
                 "en": "Cycle",
                 "fr": "Vélo",
                 "nl": "Fiets",
                 "de": "Fahrrad"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/pedestrian",
             {
                 "en": "Pedestrian",
                 "fr": "Piéton",
                 "nl": "Voetganger",
                 "de": "Fußgänger"
             })
        ], {
             "en": "Personal",
             "nl": "Persoonlijk vervoer",
             "fr": "Modes personnels",
             "de": "Individualverkehr"
         }),
        ([
            ("https://w3id.org/mobilitydcat-ap/transport-mode/other",
             {
                 "en": "Other",
                 "fr": "Autre",
                 "nl": "Andere",
                 "de": "Andere"
             })
        ], {
             "en": "Not applicable",
             "nl": "Niet toepasbaar",
             "fr": "Non applicable",
             "de": "Nicht anwendbar"
         }
        )
]



def get_translated_category_and_sub_category():
    return MOBILITY_THEME


def filter_default_tags_only(items):
    filtered_items = []
    tags = []
    for categorized_tags in get_translated_tags():
        for translated_tag in categorized_tags[0]:
            tags.append(translated_tag[0])
    for item in items:
        for tag in tags:
            if benap_tag_mapping(item['name']) == tag:
                filtered_items.append(item)
    return filtered_items


def is_default_tag(item):
    for categorized_tags in get_translated_tags():
        for translated_tag in categorized_tags[0]:
            if item['name'] == translated_tag[0]:
                return True
    show_element(item)
    return False


def getTranslatedVideoUrl(lang):
    switcher = {
        'en': 'https://www.youtube.com/embed/0-M48xzlWzI?rel=0&enablejsapi=1',
        'nl': 'https://www.youtube.com/embed/jle8RPRW1Do?rel=0&enablejsapi=1',
        'fr': 'https://www.youtube.com/embed/p8b9hIYM9hE?rel=0&enablejsapi=1',
        'de': 'https://www.youtube.com/embed/kB75uVs8oVo?rel=0&enablejsapi=1'
    }
    return switcher.get(lang, switcher.get('en'))


def get_organization_by_id(id):
    user = toolkit.get_action('get_site_user')(
        {
            'ignore_auth': True
        },
        {})

    context = {'user': user['name']}

    organization = toolkit.get_action('organization_show')(context,
    {
        'id': id,
        'include_dataset_count':False,
        'include_users': False,
        'include_groups': False,
        'include_tags': False,
        'include_followers': False,
    })
    field = 'display_title_' + user_language()
    to_show_name = organization.get(field)

    if (to_show_name):
        return to_show_name
    else:
        return organization.get('display_name')


def show_element(x):
    return x


def benap_fluent_label(field_name, field_label, lang):
    """
    Return a label for the input label for the given language
    """
    schema = scheming_get_dataset_schema('dataset')
    if schema:
        field_metadata = [x for x in schema['dataset_fields'] if x['field_name'] == field_name]
        if len(field_metadata) > 0:
            return field_metadata[0]['label'][lang]

    return field_label

def is_user_sysAdmin(user):
    userFetched = toolkit.get_action('user_show')(data_dict={'id':user})
    if userFetched.get('sysadmin') is not None and userFetched['sysadmin'] :
        return True
    return False

def is_nap_checked(datasetID):
    if not datasetID:
        return "False"
    datasetFetched = toolkit.get_action('package_show')(data_dict={'id':datasetID})
    return "True" if datasetFetched.get("nap_checked") is not None and datasetFetched['nap_checked'] else "False"

def convert_validation_list_to_JSON(data):
    """
    Converts a string containing a JSON-like structure into a proper JSON list format.

    If the input string contains curly braces ('{', '}'), it is assumed to be a
    JSON-like structure and is converted by replacing the curly braces with square
    brackets ('[', ']'). If not, the string is wrapped in a JSON array format.

    This function is particularly useful for handling cases where a validation
    process converts a JSON string into a list format unexpectedly.
    """
    if '{' in data:
        data_string = data.replace('{', '[').replace('}', ']')
    else:
        data_string = '["{}"]'.format(data)
    return data_string

def benap_get_organization_field_by_id(org_id, field_name):
    """
    Retrieve the specified field value from an organization's data based on the organization id.
    """
    user = toolkit.get_action('get_site_user')(
        {
            'ignore_auth': True
        },
        {})
    context = {'user': user['name']}
    org_data = toolkit.get_action('organization_show')(context,
                                                        {
                                                            'id': org_id,
                                                            'include_dataset_count': False,
                                                            'include_users': False,
                                                            'include_groups': False,
                                                            'include_tags': False,
                                                            'include_followers': False,
                                                        })

    field_value = org_data.get(field_name)
    return field_value

def benap_get_organization_field_by_specified_field(org_value, field_name, search_field):
    """
    Retrieve the specified field value from an organization's data based on a specified search field.
    """
    from ckantoolkit import h
    org_list = h.organizations_available('create_dataset')

    org_data = next((org for org in org_list if org.get(search_field) == org_value), None)

    if org_data is None:
        return None

    field_value = org_data.get(field_name)
    return field_value

def benap_retrieve_dict_items_or_keys_or_values(data, return_type):
    """
    Retrieve keys, values, or both from a JSON-encoded dictionary.
    """
    if data:
        data = json.loads(data)

        if return_type == "keys":
            return list(data.keys())
        elif return_type == "values":
            return list(chain.from_iterable(list(data.values())))
        elif return_type == "items":
            return list(data.items())
    else:
        return []

def benap_retrieve_org_title_tel_email():
    """
    Retrieves a list of organizations where the current user can create datasets,
    including only the organization's title, telephone number, and email.
    """
    from ckantoolkit import h
    user = toolkit.get_action('get_site_user')(
        {
            'ignore_auth': True
        },
        {})
    context = {'user': user['name']}

    # organization_list has a limit of 25 orgs request at a time when all_fields is enabled
    # https://github.com/ckan/ckan/blob/2.11/ckan/logic/action/get.py#L346
    start = 0
    batch_size = 25
    all_orgs = []

    while True:
        batch = toolkit.get_action('organization_list')({}, {
            'include_dataset_count': False,
            'all_fields': True,
            'include_extras': True,
            'limit': batch_size,
            'offset': start
        })

        if not batch:
            break

        all_orgs.extend(batch)
        start += batch_size   
    keys_to_keep = ["title", "do_tel", "do_email"]
    filtered_props = [
        {key: item.get(key) for key in keys_to_keep}
        for item in all_orgs
    ]
    return filtered_props

def benap_retrieve_raw_choices_list(field_name):
    """
    Retrieve the raw choices list of a specified field
    """
    from ckanext.benap.helpers import lists
    return getattr(lists, field_name.upper())

def benap_tag_update_helper(data, choices):
    """
    Helper to remove old unused tags
    """
    if data:
        elements = data.split(',')
        valid_choices = [item[0] for sublist, _ in choices for item in sublist]
        filtered_elements = [element for element in elements if element in valid_choices]
        filtered_data = ','.join(filtered_elements)

        return filtered_data

    else:
        return None

def benap_tag_mapping(tag_name):
    """
    Create dictionary of tag mapping (tag name in table tag and url in table package_extra, fluent_tags)
    """
    urls = [item[0] for sublist, _ in get_translated_tags() for item in sublist]
    tag_mapping = {
        url.split("/")[-1].capitalize(): url
        for url in urls
    }
    return tag_mapping.get(tag_name)


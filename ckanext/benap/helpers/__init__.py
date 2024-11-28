# coding=utf-8
import json
import ckan.plugins.toolkit as toolkit
from ckan.common import config
import logging
from decorators import decorator_timer
from itertools import chain


from ckanext.benap.helpers.lists import (NUTS1_BE, GEOREFERENCING_METHOD, DATASET_TYPE, NAP_TYPE, NETWORK_COVERAGE,
                                         MOBILITY_THEME, CONDITIONS_USAGE, CONDITIONS_ACCESS, LICENSE_TYPE, FREQUENCY, \
                                         REFERENCE_SYSTEM)

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

    elif ontology == "EU-language":
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
    elif ontology == "EU_COUNTRY":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/country/BEL', {
                "en": u"Belgium",
                "fr": u"Belgique",
                "nl": u"België",
                "de": u"Belgien"
            }),
            ('http://publications.europa.eu/resource/authority/country/NLD', {
                "en": u"Netherlands",
                "fr": u"Pays-Bas",
                "nl": u"Nederland",
                "de": u"Niederlande"
            }),
            ('http://publications.europa.eu/resource/authority/country/FRA', {
                "en": u"France",
                "fr": u"France",
                "nl": u"Frankrijk",
                "de": u"Frankreich"
            }),
            ('http://publications.europa.eu/resource/authority/country/DEU', {
                "en": u"Germany",
                "fr": u"Allemagne",
                "nl": u"Duitsland",
                "de": u"Deutschland"
            }),
            ('http://publications.europa.eu/resource/authority/country/LUX', {
                "en": u"Luxembourg",
                "fr": u"Luxembourg",
                "nl": u"Luxemburg",
                "de": u"Luxemburg"
            }),
            ('http://publications.europa.eu/resource/authority/country/GBR', {
                "en": u"United Kingdom",
                "fr": u"Royaume-Uni",
                "nl": u"Verenigd Koninkrijk",
                "de": u"Vereinigtes Königreich"
            }),
            ('http://publications.europa.eu/resource/authority/country/BGR', {
                "en": u"Bulgaria",
                "fr": u"Bulgarie",
                "nl": u"Bulgarije",
                "de": u"Bulgarien"
            }),
            ('http://publications.europa.eu/resource/authority/country/CZE', {
                "en": u"Czechia",
                "fr": u"Tchéquie",
                "nl": u"Tsjechië",
                "de": u"Tschechien"
            }),
            ('http://publications.europa.eu/resource/authority/country/DNK', {
                "en": u"Denmark",
                "fr": u"Danemark",
                "nl": u"Denemarken",
                "de": u"Dänemark"
            }),
            ('http://publications.europa.eu/resource/authority/country/EST', {
                "en": u"Estonia",
                "fr": u"Estonie",
                "nl": u"Estland",
                "de": u"Estland"
            }),
            ('http://publications.europa.eu/resource/authority/country/IRL', {
                "en": u"Ireland",
                "fr": u"Irlande",
                "nl": u"Ierland",
                "de": u"Irland"
            }),
            ('http://publications.europa.eu/resource/authority/country/GRC', {
                "en": u"Greece",
                "fr": u"Grèce",
                "nl": u"Griekenland",
                "de": u"Griechenland"
            }),
            ('http://publications.europa.eu/resource/authority/country/ESP', {
                "en": u"Spain",
                "fr": u"Espagne",
                "nl": u"Spanje",
                "de": u"Spanien"
            }),
            ('http://publications.europa.eu/resource/authority/country/HRV', {
                "en": u"Croatia",
                "fr": u"Croatie",
                "nl": u"Kroatië",
                "de": u"Kroatien"
            }),
            ('http://publications.europa.eu/resource/authority/country/ITA', {
                "en": u"Italy",
                "fr": u"Italie",
                "nl": u"Italië",
                "de": u"Italien"
            }),
            ('http://publications.europa.eu/resource/authority/country/CYP', {
                "en": u"Cyprus",
                "fr": u"Chypre",
                "nl": u"Cyprus",
                "de": u"Zypern"
            }),
            ('http://publications.europa.eu/resource/authority/country/LVA', {
                "en": u"Latvia",
                "fr": u"Lettonie",
                "nl": u"Letland",
                "de": u"Lettland"
            }),
            ('http://publications.europa.eu/resource/authority/country/LTU', {
                "en": u"Lithuania",
                "fr": u"Lituanie",
                "nl": u"Litouwen",
                "de": u"Litauen"
            }),
            ('http://publications.europa.eu/resource/authority/country/HUN', {
                "en": u"Hungary",
                "fr": u"Hongrie",
                "nl": u"Hongarije",
                "de": u"Ungarn"
            }),
            ('http://publications.europa.eu/resource/authority/country/MLT', {
                "en": u"Malta",
                "fr": u"Malte",
                "nl": u"Malta",
                "de": u"Malta"
            }),
            ('http://publications.europa.eu/resource/authority/country/AUT', {
                "en": u"Austria",
                "fr": u"Autriche",
                "nl": u"Oostenrijk",
                "de": u"Österreich"
            }),
            ('http://publications.europa.eu/resource/authority/country/POL', {
                "en": u"Poland",
                "fr": u"Pologne",
                "nl": u"Polen",
                "de": u"Polen"
            }),
            ('http://publications.europa.eu/resource/authority/country/PRT', {
                "en": u"Portugal",
                "fr": u"Portugal",
                "nl": u"Portugal",
                "de": u"Portugal"
            }),
            ('http://publications.europa.eu/resource/authority/country/ROU', {
                "en": u"Romania",
                "fr": u"Roumanie",
                "nl": u"Roemenië",
                "de": u"Rumänien"
            }),
            ('http://publications.europa.eu/resource/authority/country/SVN', {
                "en": u"Slovenia",
                "fr": u"Slovénie",
                "nl": u"Slovenië",
                "de": u"Slowenien"
            }),
            ('http://publications.europa.eu/resource/authority/country/SVK', {
                "en": u"Slovakia",
                "fr": u"Slovaquie",
                "nl": u"Slowakije",
                "de": u"Slowakei"
            }),
            ('http://publications.europa.eu/resource/authority/country/FIN', {
                "en": u"Finland",
                "fr": u"Finlande",
                "nl": u"Finland",
                "de": u"Finnland"
            }),
            ('http://publications.europa.eu/resource/authority/country/SWE', {
                "en": u"Sweden",
                "fr": u"Suède",
                "nl": u"Zweden",
                "de": u"Schweden"
            }),
        ])
    elif ontology == "NUTS1_BE":
        return map_for_form_select(NUTS1_BE)
    elif ontology == "NUTS3_BE":
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
            ('http://data.europa.eu/nuts/code/BE321', {
                "en": u"Arr. Ath",
                "fr": u"Arr. Ath",
                "nl": u"Arr. Ath",
                "de": u"Arr. Ath"
            }),
            ('http://data.europa.eu/nuts/code/BE322', {
                "en": u"Arr. Charleroi",
                "fr": u"Arr. Charleroi",
                "nl": u"Arr. Charleroi",
                "de": u"Arr. Charleroi"
            }),
            ('http://data.europa.eu/nuts/code/BE323', {
                "en": u"Arr. Mons",
                "fr": u"Arr. Mons",
                "nl": u"Arr. Mons",
                "de": u"Arr. Mons"
            }),
            ('http://data.europa.eu/nuts/code/BE324', {
                "en": u"Arr. Mouscron",
                "fr": u"Arr. Mouscron",
                "nl": u"Arr. Mouscron",
                "de": u"Arr. Mouscron"
            }),
        ])

    elif ontology == "encoding":
        return map_for_form_select([
            ('ASCII', {
                "en": u"ASCII",
                "fr": u"ASCII",
                "nl": u"ASCII",
                "de": u"ASCII"
            }),
            ('UTF-8', {
                "en": u"UTF-8",
                "fr": u"UTF-8",
                "nl": u"UTF-8",
                "de": u"UTF-8"
            }),
            ('UTF-16', {
                "en": u"UTF-16",
                "fr": u"UTF-16",
                "nl": u"UTF-16",
                "de": u"UTF-16"
            }),
            ('ISO-8859-1', {
                "en": u"ISO-8859-1",
                "fr": u"ISO-8859-1",
                "nl": u"ISO-8859-1",
                "de": u"ISO-8859-1"
            }),
            ('ISO-8859-15', {
                "en": u"ISO-8859-15",
                "fr": u"ISO-8859-15",
                "nl": u"ISO-8859-15",
                "de": u"ISO-8859-15"
            }),
            ('Other', {
                "en": u"Other",
                "fr": u"Autre",
                "nl": u"Andere",
                "de": u"Andere"
            }),
        ])

    elif ontology == "syntax":
        return map_for_form_select([
            ('XML', {
                "en": u"XML",
                "fr": u"XML",
                "nl": u"XML",
                "de": u"XML"
            }),
            ('JSON', {
                "en": u"JSON",
                "fr": u"JSON",
                "nl": u"JSON",
                "de": u"JSON"
            }),
            ('CSV', {
                "en": u"CSV",
                "fr": u"CSV",
                "nl": u"CSV",
                "de": u"CSV"
            }),
            ('ASN.1 encoding rules', {
                "en": u"ASN.1 encoding rules",
                "fr": u"Règles d'encodage d'ASN.1",
                "nl": u"ASN.1 coderingsregels",
                "de": u"ASN.1 Kodierunsregel"
            }),
            ('Protocol buffers', {
                "en": u"Protocol buffers",
                "fr": u"Tampons de protocole",
                "nl": u"Protocolbuffers",
                "de": u"Protokoll-Buffer"
            }),
            ('Other', {
                "en": u"Other",
                "fr": u"Autre",
                "nl": u"Andere",
                "de": u"Andere"
            }),
        ])

    elif ontology == "grammar":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/file-type/SCHEMA_XML', {
                "en": u"XSD",
                "fr": u"XSD",
                "nl": u"XSD",
                "de": u"XSD"
            }),
            ('JSON Schema', {
                "en": u"JSON Schema",
                "fr": u"Schéma JSON",
                "nl": u"JSON-schema",
                "de": u"JSON-Schema"
            }),
            ('http://purl.org/ASN/schema/core/StandardDocument', {
                "en": u"ASN.1",
                "fr": u"ASN.1",
                "nl": u"ASN.1",
                "de": u"ASN.1"
            }),
            ('Protocol buffers', {
                "en": u"Protocol buffers",
                "fr": u"Tampons de protocole",
                "nl": u"Protocolbuffers",
                "de": u"Protokoll-Buffer"
            }),
            ('Other', {
                "en": u"Other",
                "fr": u"Autre",
                "nl": u"Andere",
                "de": u"Andere"
            }),
        ])

    elif ontology == "datamodel":
        return map_for_form_select([
            ('DATEX II profile', {
                "en": u"DATEX II profile",
                "fr": u"Profil DATEX II",
                "nl": u"DATEX II profiel",
                "de": u"DATEX II-Profil"
            }),
            ('OCIT-C', {
                "en": u"OCIT-C",
                "fr": u"OCIT-C",
                "nl": u"OCIT-C",
                "de": u"OCIT-C"
            }),
            ('DATEX II Light', {
                "en": u"DATEX II Light",
                "fr": u"DATEX II Light",
                "nl": u"DATEX II Light",
                "de": u"DATEX II Light"
            }),
            ('NeTEX', {
                "en": u"NeTEX (CEN/TS 16614)",
                "fr": u"NeTEX (CEN/TS 16614)",
                "nl": u"NeTEX (CEN/TS 16614)",
                "de": u"NeTEX (CEN/TS 16614)"
            }),
            ('SIRI', {
                "en": u"SIRI (CEN/TS 15531)",
                "fr": u"SIRI (CEN/TS 15531)",
                "nl": u"SIRI (CEN/TS 15531)",
                "de": u"SIRI (CEN/TS 15531)"
            }),
            ('GTFS', {
                "en": u"GTFS",
                "fr": u"GTFS",
                "nl": u"GTFS",
                "de": u"GTFS"
            }),
            ('GBFS', {
                "en": u"GBFS",
                "fr": u"GBFS",
                "nl": u"GBFS",
                "de": u"GBFS"
            }),
            ('MDS', {
                "en": u"MDS",
                "fr": u"MDS",
                "nl": u"MDS",
                "de": u"MDS"
            }),
            ('VDV Standard', {
                "en": u"VDV Standard (VDV 452, 455, 462,…)",
                "fr": u"VDV Standard (VDV 452, 455, 462,…)",
                "nl": u"VDV Standard (VDV 452, 455, 462,…)",
                "de": u"VDV Standard (VDV 452, 455, 462,…)"
            }),
            ('IFOPT', {
                "en": u"IFOPT",
                "fr": u"IFOPT",
                "nl": u"IFOPT",
                "de": u"IFOPT"
            }),
            ('ETSI / ISO Model', {
                "en": u"ETSI / ISO Model (DENM, CAM, SPAT/MAP, IVI,…)",
                "fr": u"ETSI / ISO Model (DENM, CAM, SPAT/MAP, IVI,…)",
                "nl": u"ETSI / ISO Model (DENM, CAM, SPAT/MAP, IVI,…)",
                "de": u"ETSI / ISO Model (DENM, CAM, SPAT/MAP, IVI,…)"
            }),
            ('tpegML Model', {
                "en": u"tpegML Model (TPEG2-TEC, TPEG2-PKI,…)",
                "fr": u"tpegML Model (TPEG2-TEC, TPEG2-PKI,…)",
                "nl": u"tpegML Model (TPEG2-TEC, TPEG2-PKI,…)",
                "de": u"tpegML Model (TPEG2-TEC, TPEG2-PKI,…)"
            }),
            ('http://publications.europa.eu/resource/authority/file-type/KML', {
                "en": u"KML",
                "fr": u"KML",
                "nl": u"KML",
                "de": u"KML"
            }),

            ('http://publications.europa.eu/resource/authority/file-type/MPEG4', {
                "en": u"MPEG-4",
                "fr": u"MPEG-4",
                "nl": u"MPEG-4",
                "de": u"MPEG-4"
            }),
            ('MDM-Container', {
                "en": u"MDM-Container",
                "fr": u"MDM-Container",
                "nl": u"MDM-Container",
                "de": u"MDM-Container"
            }),
            ('DINO', {
                "en": u"DINO",
                "fr": u"DINO",
                "nl": u"DINO",
                "de": u"DINO"
            }),
            ('OpenAPI', {
                "en": u"OpenAPI",
                "fr": u"OpenAPI",
                "nl": u"OpenAPI",
                "de": u"OpenAPI"
            }),
            ('Other', {
                "en": u"Other",
                "fr": u"Autre",
                "nl": u"Andere",
                "de": u"Andere"
            }),
        ])

    elif ontology == "protocol":
        return map_for_form_select([
            ('SOAP', {
                "en": u"SOAP",
                "fr": u"SOAP",
                "nl": u"SOAP",
                "de": u"SOAP"
            }),
            ('OTS2', {
                "en": u"OTS2",
                "fr": u"OTS2",
                "nl": u"OTS2",
                "de": u"OTS2"
            }),
            ('http://publications.europa.eu/resource/authority/file-type/MSG_HTTP', {
                "en": u"HTTP/HTTPS",
                "fr": u"HTTP/HTTPS",
                "nl": u"HTTP/HTTPS",
                "de": u"HTTP/HTTPS"
            }),
            ('FTP', {
                "en": u"FTP",
                "fr": u"FTP",
                "nl": u"FTP",
                "de": u"FTP"
            }),
            ('http://publications.europa.eu/resource/authority/file-type/RSS', {
                "en": u"RSS",
                "fr": u"RSS",
                "nl": u"RSS",
                "de": u"RSS"
            }),
            ('AMQP', {
                "en": u"AMQP",
                "fr": u"AMQP",
                "nl": u"AMQP",
                "de": u"AMQP"
            }),
            ('MQTT', {
                "en": u"MQTT",
                "fr": u"MQTT",
                "nl": u"MQTT",
                "de": u"MQTT"
            }),
            ('gRPC', {
                "en": u"gRPC",
                "fr": u"gRPC",
                "nl": u"gRPC",
                "de": u"gRPC"
            }),
            ('Other', {
                "en": u"Other",
                "fr": u"Autre",
                "nl": u"Andere",
                "de": u"Andere"
            }),
        ])

    elif ontology == "communication":
        return map_for_form_select([
            ('Push', {
                "en": u"Push",
                "fr": u"Push",
                "nl": u"Push",
                "de": u"Push"
            }),
            ('Push on occurence', {
                "en": u"Push on occurrence",
                "fr": u"Push on occurrence",
                "nl": u"Push on occurrence",
                "de": u"Push on occurrence"
            }),
            ('Pull', {
                "en": u"Pull",
                "fr": u"Pull",
                "nl": u"Pull",
                "de": u"Pull"
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


def translate_organization_filter(facet_title, lang):
    translated_titles = {"en": "Organizations", "nl": "Organisaties", "fr": "Organisations", "de": "Organisationen"}
    if facet_title == "Organizations":
        return translated_titles[lang]
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
    return map(lambda org: org['title'].encode("utf-8"), h.organizations_available('create_dataset'))


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
        return filter(lambda x: x[0] == tag['name'], [translated_tag for translated_taglist in
                                                      [categorized_tags[0] for categorized_tags in
                                                       tags] for translated_tag in
                                                      translated_taglist])[0][1][lang]
    except:
        try:
            return tag['display_name']
        except KeyError:
            try:
                if isinstance(tag, str):
                    return tag
                print('tag not found: ' + json.dumps(tag))
            except:
                print('tag not found')


def get_translated_tags():
    return [
        ([
            ("https://w3id.org/mobilitydcat-ap/transport-mode/air",
             {
                 "en": u"Air",
                 "fr": u"Aérien",
                 "nl": u"Vliegtuig",
                 "de": u"Luftverkehr"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/long-distance-rail",
             {
                 "en": u"Rail (including high speed rail)",
                 "fr": u"Ferroviaire (y compris ferroviaire à grande vitesse)",
                 "nl": u"Trein (m.i.v. hogesnelheidstrein)",
                 "de": u"Eisenbahn (einschl. Hochgeschwindigkeit)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/regional-and-local-rail",
             {
                 "en": u"Conventional rail",
                 "fr": u"Ferroviaire conventionnel",
                 "nl": u"Klassieke trein",
                 "de": u"Konventioneller Bahnverkehr"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/long-distance-coach",
             {
                 "en": u"Long-distance coach",
                 "fr": u"Autocar longue distance",
                 "nl": u"Langeafstandsbus",
                 "de": u"Fernbus"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/maritime",
             {
                 "en": u"Maritime (including ferry)",
                 "fr": u"Maritime (y compris les ferries)",
                 "nl": u"Schip (m.i.v. veerboten)",
                 "de": u"Schifffahrt (einschließlich Fähre)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/metro-subway-train",
             {
                 "en": u"Metro",
                 "fr": u"Métro",
                 "nl": u"Metro",
                 "de": u"Untergrundbahn"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/tram-light-rail",
             {
                 "en": u"Tram, Light rail",
                 "fr": u"Tram, Ferroviaire léger",
                 "nl": u"Tram, Light rail",
                 "de": u"Straßenbahn, Stadtbahn"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/bus",
             {
                 "en": u"Bus",
                 "fr": u"Bus",
                 "nl": u"Bus",
                 "de": u"Bus"
             })
        ], {
             "en": u"Scheduled",
             "nl": u"Openbaar vervoer",
             "fr": u"Services réguliers",
             "de": u"Linienverkehrsdienste"
         }),
        ([
            ("https://w3id.org/mobilitydcat-ap/transport-mode/shuttle-bus",
             {
                 "en": u"Shuttle bus",
                 "fr": u"Bus",
                 "nl": u"Shuttlebus",
                 "de": u"Pendelbus"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/shuttle-ferry",
             {
                 "en": u"Shuttle ferry",
                 "fr": u"Ferry",
                 "nl": u"Shuttleveerboot",
                 "de": u"Pendelfähre"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/taxi",
             {
                 "en": u"Taxi",
                 "fr": u"Taxi",
                 "nl": u"Taxi",
                 "de": u"Taxi"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/car-sharing",
             {
                 "en": u"Car-sharing",
                 "fr": u"Voitures partagées",
                 "nl": u"Deelauto",
                 "de": u"Gemeinsame Pkw-Nutzung (Car-Sharing)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/car-pooling",
             {
                 "en": u"Car-pooling",
                 "fr": u"Covoiturage",
                 "nl": u"Carpooling",
                 "de": u"Fahrgemeinschaften (Car-Pooling)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/car-hire",
             {
                 "en": u"Car-hire",
                 "fr": u"Location de voitures",
                 "nl": u"Huurauto",
                 "de": u"Mietwagen"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/bike-sharing",
             {
                 "en": u"Bike-sharing",
                 "fr": u"Vélos partagés",
                 "nl": u"Deelfiets",
                 "de": u"Gemeinsame Nutzung von Fahrrädern (Bike-Sharing)"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/bike-hire",
             {
                 "en": u"Bike-hire",
                 "fr": u"Vélos en libre service",
                 "nl": u"Huurfiets",
                 "de": u"Leihfahrrad"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/ride-pooling",
             {
                 "en": u"Ride-pooling",
                 "fr": u"Trajets partagés",
                 "nl": u"Gedeelde ritten",
                 "de": u"Mitfahrdienst"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/e-scooter",
             {
                 "en": u"E-scooter",
                 "fr": u"Trottinettes électriques",
                 "nl": u"E-scooter",
                 "de": u"E-rollern"
             })
        ], {
             "en": u"Demand-responsive",
             "nl": u"Aanbod afhankelijke inzet",
             "fr": u"Services à la demande",
             "de": u"Abruf-Verkehrsdienste"
         }),
        ([
            ("https://w3id.org/mobilitydcat-ap/transport-mode/car",
             {
                 "en": u"Car",
                 "fr": u"Voiture",
                 "nl": u"Auto",
                 "de": u"Pkw"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/truck",
             {
                 "en": u"Truck",
                 "fr": u"Camion",
                 "nl": u"Vrachtwagen",
                 "de": u"Lastwagen"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/motorcycle",
             {
                 "en": u"Motorcycle",
                 "fr": u"Moto",
                 "nl": u"Motorfiets",
                 "de": u"Motorrad"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/bicycle",
             {
                 "en": u"Cycle",
                 "fr": u"Vélo",
                 "nl": u"Fiets",
                 "de": u"Fahrrad"
             }),
            ("https://w3id.org/mobilitydcat-ap/transport-mode/pedestrian",
             {
                 "en": u"Pedestrian",
                 "fr": u"Piéton",
                 "nl": u"Voetganger",
                 "de": u"Fußgänger"
             })
        ], {
             "en": u"Personal",
             "nl": u"Persoonlijk vervoer",
             "fr": u"Modes personnels",
             "de": u"Individualverkehr"
         }),
        ([
            ("https://w3id.org/mobilitydcat-ap/transport-mode/other",
             {
                 "en": u"Other",
                 "fr": u"Autre",
                 "nl": u"Andere",
                 "de": u"Andere"
             })
        ], {
             "en": u"Not applicable",
             "nl": u"Niet toepasbaar",
             "fr": u"Non applicable",
             "de": u"Nicht anwendbar"
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
            if item['name'] == tag:
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
    user = toolkit.get_action(u'get_site_user')(
        {
            u'ignore_auth': True
        },
        {})

    context = {u'user': user[u'name']}

    organization = toolkit.get_action(u'organization_show')(context,
    {
        u'id': id,
        u'include_dataset_count':False,
        u'include_users': False,
        u'include_groups': False,
        u'include_tags': False,
        u'include_followers': False,
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
        field_metadata = filter(lambda x: x['field_name'] == field_name, schema['dataset_fields'])
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
    user = toolkit.get_action(u'get_site_user')(
        {
            u'ignore_auth': True
        },
        {})
    context = {u'user': user[u'name']}
    org_data = toolkit.get_action(u'organization_show')(context,
                                                        {
                                                            u'id': org_id,
                                                            u'include_dataset_count': False,
                                                            u'include_users': False,
                                                            u'include_groups': False,
                                                            u'include_tags': False,
                                                            u'include_followers': False,
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
            return list(chain.from_iterable(data.values()))
        elif return_type == "items":
            return data.items()
    else:
        return []

def benap_retrieve_org_title_tel_email():
    """
    Retrieves a list of organizations where the current user can create datasets,
    including only the organization's title, telephone number, and email.
    """
    from ckantoolkit import h
    user = toolkit.get_action(u'get_site_user')(
        {
            u'ignore_auth': True
        },
        {})
    context = {u'user': user[u'name']}
    available_orgs_for_user = [org['name'].encode("utf-8") for org in h.organizations_available('create_dataset')]
    data = toolkit.get_action(u'organization_list')(context,
                                                    {
                                                        u'include_dataset_count': False,
                                                        u'all_fields': True,
                                                        u'include_users': False,
                                                        u'include_groups': False,
                                                        u'include_tags': False,
                                                        u'include_followers': False,
                                                        u'include_extras': True,
                                                        u'organizations': available_orgs_for_user
                                                    })
    keys_to_keep = ["title", "do_tel", "do_email"]
    filtered_data = [
        {key: item.get(key) for key in keys_to_keep}
        for item in data
    ]
    json_data = json.dumps(filtered_data, ensure_ascii=False)
    return json_data

def benap_retrieve_raw_choices_list(field_name):
    """
    Retrieve the raw choices list of a specified field
    """
    from ckanext.benap.helpers import lists
    return getattr(lists, field_name.upper())

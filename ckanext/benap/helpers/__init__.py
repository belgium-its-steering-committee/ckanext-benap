# coding=utf-8

from ckanext.benap.util.forms import map_for_form_select


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

    if ontology == "encoding":
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
                "fr": u"Other",
                "nl": u"Other",
                "de": u"Other"
            }),
        ])

    if ontology == "syntax":
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
            ('http://purl.org/ASN/schema/core/StandardDocument', {
                "en": u"ASN.1 encoding rules",
                "fr": u"ASN.1 encoding rules",
                "nl": u"ASN.1 encoding rules",
                "de": u"ASN.1 encoding rules"
            }),
            ('Protocol buffers', {
                "en": u"Protocol buffers",
                "fr": u"Protocol buffers",
                "nl": u"Protocol buffers",
                "de": u"Protocol buffers"
            }),
            ('Other', {
                "en": u"Other",
                "fr": u"Other",
                "nl": u"Other",
                "de": u"Other"
            }),
        ])

    if ontology == "grammar":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/file-type/SCHEMA_XML', {
                "en": u"XSD",
                "fr": u"XSD",
                "nl": u"XSD",
                "de": u"XSD"
            }),
            ('JSON Schema', {
                "en": u"JSON Schema",
                "fr": u"JSON Schema",
                "nl": u"JSON Schema",
                "de": u"JSON Schema"
            }),
            ('http://purl.org/ASN/schema/core/StandardDocument', {
                "en": u"ASN.1",
                "fr": u"ASN.1",
                "nl": u"ASN.1",
                "de": u"ASN.1"
            }),
            ('Protocol buffers', {
                "en": u"Protocol buffers",
                "fr": u"Protocol buffers",
                "nl": u"Protocol buffers",
                "de": u"Protocol buffers"
            }),
            ('Other', {
                "en": u"Other",
                "fr": u"Other",
                "nl": u"Other",
                "de": u"Other"
            }),
        ])

    if ontology == "datamodel":
        return map_for_form_select([
            ('DATEX II profile', {
                "en": u"DATEX II profile",
                "fr": u"DATEX II profile",
                "nl": u"DATEX II profile",
                "de": u"DATEX II profile"
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
                "fr": u"Other",
                "nl": u"Other",
                "de": u"Other"
            }),
        ])

    if ontology == "protocol":
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
                "fr": u"Other",
                "nl": u"Other",
                "de": u"Other"
            }),
        ])

    if ontology == "communication":
        return map_for_form_select([
            ('Push', {
                "en": u"Push",
                "fr": u"Push",
                "nl": u"Push",
                "de": u"Push"
            }),
            ('Push on occurence', {
                "en": u"Push on occurence",
                "fr": u"Push on occurence",
                "nl": u"Push on occurence",
                "de": u"Push on occurence"
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
        return map_for_form_select([
            ('On occurence', {
                "en": u"On occurence",
                "fr": u"On occurence",
                "nl": u"On occurence",
                "de": u"On occurence"
            }),
            ('Up to 1min', {
                "en": u"Up to 1min",
                "fr": u"Up to 1min",
                "nl": u"Up to 1min",
                "de": u"Up to 1min"
            }),
            ('Up to 5min', {
                "en": u"Up to 5min",
                "fr": u"Up to 5min",
                "nl": u"Up to 5min",
                "de": u"Up to 5min"
            }),
            ('Up to 10min', {
                "en": u"Up to 10min",
                "fr": u"Up to 10min",
                "nl": u"Up to 10min",
                "de": u"Up to 10min"
            }),
            ('Up to 15min', {
                "en": u"Up to 15min",
                "fr": u"Up to 15min",
                "nl": u"Up to 15min",
                "de": u"Up to 15min"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/BIHOURLY', {
                "en": u"Up to 30min",
                "fr": u"Up to 30min",
                "nl": u"Up to 30min",
                "de": u"Up to 30min"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/HOURLY', {
                "en": u"Up to 1h",
                "fr": u"Up to 1h",
                "nl": u"Up to 1h",
                "de": u"Up to 1h"
            }),
            ('Up to 2h', {
                "en": u"Up to 2h",
                "fr": u"Up to 2h",
                "nl": u"Up to 2h",
                "de": u"Up to 2h"
            }),
            ('Up to 3h', {
                "en": u"Up to 3h",
                "fr": u"Up to 3hn",
                "nl": u"Up to 3h",
                "de": u"Up to 3h"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/DAILY_2', {
                "en": u"Up to 12h",
                "fr": u"Up to 12h",
                "nl": u"Up to 12h",
                "de": u"Up to 12h"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/DAILY', {
                "en": u"Up to 24h",
                "fr": u"Up to 24h",
                "nl": u"Up to 24h",
                "de": u"Up to 24h"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/WEEKLY', {
                "en": u"Up to Weekly",
                "fr": u"Up to Weekly",
                "nl": u"Up to Weekly",
                "de": u"Up to Weekly"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/MONTHLY', {
                "en": u"Up to Monthly",
                "fr": u"Up to Monthly",
                "nl": u"Up to Monthly",
                "de": u"Up to Monthly"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/QUARTERLY', {
                "en": u"Up to every 3month",
                "fr": u"Up to every 3month",
                "nl": u"Up to every 3month",
                "de": u"Up to every 3month"
            }),
            ('http://publications.europa.eu/resource/authority/frequency/ANNUAL_2', {
                "en": u"Up to every 6month",
                "fr": u"Up to every 6month",
                "nl": u"Up to every 6month",
                "de": u"Up to every 6month"
            }),
            ('Uhttp://publications.europa.eu/resource/authority/frequency/ANNUAL', {
                "en": u"Up to yearly",
                "fr": u"Up to yearly",
                "nl": u"Up to yearly",
                "de": u"Up to yearly"
            }),
            ('Less frequent than yearly', {
                "en": u"Less frequent than yearly",
                "fr": u"Less frequent than yearly",
                "nl": u"Less frequent than yearly",
                "de": u"Less frequent than yearly"
            }),

        ])
    return None


def scheming_language_text_fallback(field_data, language_data):
    return field_data['en'] or field_data['nl'] or field_data['fr'] or field_data['de']

# coding=utf-8
from ckanext.benap.constants.concept_collections.nuts import NUTS1_BE
from ckanext.benap.constants.concept_collections.mobilitydcat.georeferencing_method import GEOREFERENCING_METHOD
from ckanext.benap.constants.concept_collections.mobilitydcat.network_coverage import NETWORK_COVERAGE
from ckanext.benap.constants.concept_collections.mobilitydcat.conditions_access_usage import ACCESS as CONDITIONS_ACCESS, USAGE as CONDITIONS_USAGE
from ckanext.benap.constants.concept_collections.eu_authority.license_type import LICENSE_TYPE as LICENSE_TYPE_CONCEPTS
from ckanext.benap.constants.concept_collections.mobilitydcat.grammar import GRAMMAR
from ckanext.benap.constants.concept_collections.mobilitydcat.communication_method import COMMUNICATION_METHOD
from ckanext.benap.constants.concept_collections.mobilitydcat.application_layer_protocol import APPLICATION_LAYER_PROTOCOL
from ckanext.benap.constants.concept_collections.eu_authority.frequency import FREQUENCY
from ckanext.benap.constants.concept_collections.mobilitydcat.mobility_data_standard import MOBILITY_DATA_STANDARD as DATA_MODEL
from ckanext.benap.constants.concept_collections.eu_authority.file_type import FILE_TYPE as SYNTAX
from ckanext.benap.constants.concept_collections.opengis_crs import REFERENCE_SYSTEM

DATASET_TYPE = [
            ('Static road network data', {
                "en": "Static road network data",
                "fr": "Données routières statiques",
                "nl": "Statische weggegevens",
                "de": "Statische Straβendaten"
            }),
            ('Static traffic signs and regulations', {
                "en": "Static traffic signs and regulations",
                "fr": "Panneaux routiers et réglementations statiques",
                "nl": "Statische verkeerssignalisatie en verkeersregels",
                "de": "Statische Verkehrszeichen und -regelungen"
            }),
            ('Toll information', {
                "en": "Toll information",
                "fr": "Informations sur les péages",
                "nl": "Tol informatie",
                "de": "Mautangaben"
            }),
            ('Parking and rest area information', {
                "en": "Parking and rest area information",
                "fr": "Informations sur les aires de stationnement et de repos",
                "nl": "Parking en stopplaatsen informatie",
                "de": "Informationen zu Park- und Rastplätzen"
            }),
            ('Filling and charging stations', {
                "en": "Filling and charging stations",
                "fr": "Stations-services et de recharge",
                "nl": "Tankstations en laadpunten",
                "de": "Tankstellen und Ladestationen"
            }),
            ('Freight and logistics', {
                "en": "Freight and logistics",
                "fr": "Marchandises et logistique",
                "nl": "Goederen en logistiek",
                "de": "Waren und Logistik"
            }),
            ('Dynamic traffic signs and regulations', {
                "en": "Dynamic traffic signs and regulations",
                "fr": "Panneaux routiers et réglementations dynamiques",
                "nl": "Dynamische verkeerssignalisatie en verkeersregels",
                "de": "Dynamische Verkehrszeichen und -regelungen"
            }),
            ('Road work information', {
                "en": "Road work information",
                "fr": "Informations sur les travaux de voirie",
                "nl": "Wegenwerken informatie",
                "de": "Informationen zu Straβenbauarbeiten"
            }),
            ('Unexpected road events and conditions', {
                "en": "Unexpected road events and conditions",
                "fr": "Evénements et conditions de route imprévus",
                "nl": "Wegenincidenten en condities",
                "de": "Zufällige Straβenereignisse und –zustände"
            }),
            ('Road weather conditions', {
                "en": "Road weather conditions",
                "fr": "Conditions météorologiques routières",
                "nl": "Weercondities wegen",
                "de": "Straβenwetterszustände"
            }),
            ('Real-time traffic data', {
                "en": "Real-time traffic data",
                "fr": "Données en temps réel sur la circulation",
                "nl": "Real-time verkeersinformatie",
                "de": "Echtzeit-Verkehrsinformation"
            }),
            ('General information for trip-planning', {
                "en": "General information for trip-planning",
                "fr": "Informations générales pour la planification des déplacements",
                "nl": "Algemene informatie voor routeplanning",
                "de": "Allgemeine Informationen zu Routenplanung"
            }),
            ('Public transport: location information', {
                "en": "Public transport: location information",
                "fr": "Transports publics : information de localisation",
                "nl": "Openbaar vervoer: locatie informatie",
                "de": "Öffentlicher Verkehr: Standortinformation"
            }),
            ('Public transport: operational information', {
                "en": "Public transport: operational information",
                "fr": "Transports publics : informations opérationnelles",
                "nl": "Openbaar vervoer: operationele informatie",
                "de": "Öffentlicher Verkehr: operative Informationen"
            }),
            ('Public transport: fare and purchase information', {
                "en": "Public transport: fare and purchase information",
                "fr": "Transports publics : informations tarifaires et commerciales",
                "nl": "Openbaar vervoer: tarieven en ticket informatie",
                "de": "Öffentlicher Verkehr: Preis- und Kaufinformationen"
            }),
            ('Cycle network data', {
                "en": "Cycle network data",
                "fr": "Données sur le réseau cyclable",
                "nl": "Fietsnetwerk informatie",
                "de": "Daten zum Fahrradnetzwerk"
            }),
            ('Pedestrian network data', {
                "en": "Pedestrian network data",
                "fr": "Données sur le réseau piétonnier",
                "nl": "Voetgangersnetwerk informatie",
                "de": "Fuβwegenetz"
            }),
            ('Demand-responsive modes', {
                "en": "Demand-responsive modes",
                "fr": "Modes de transport à la demande",
                "nl": "Vraagafhankelijk vervoer",
                "de": "Bedarfsgesteuerte Verkehrsträger"
            }),
            ('Other', {
                "en": "Other",
                "fr": "Autres",
                "nl": "Andere",
                "de": "Anderen"
            })
        ]

NAP_TYPE = [('MMTIS', {
                "en": "MMTIS - Multimodal travel information services",
                "nl": "MMTIS - Multimodale reisinformatiediensten",
                "fr": "MMTIS - Services d'informations sur les déplacements multimodaux",
                "de": "MMTIS - Multimodaler Reiseinformationsdienste"
            }),
            ('RTTI', {
                "en": "RTTI - Real time traffic information services",
                "nl": "RTTI - Realtimeverkeersinformatiediensten",
                "fr": "RTTI - Services d'informations en temps réel sur la circulation",
                "de": "RTTI - Echtzeit Verkehrsinformationdienste"
            }),
            ('SRTI', {
                "en": "SRTI - Safety related traffic information",
                "nl": "SRTI - Verkeersveiligheidsinformatie",
                "fr": "SRTI - Information liées à la sécurité routière",
                "de": "SRTI - Straßenverkehrssicherheit relevanter Verkehrsinformationen"
            }),
            ('SSTP', {
                "en": "SSTP - Information services for safe and secure truck parkings",
                "nl": "SSTP - Informatiediensten voor veilige en beveiligde parkeerplaatsen voor vrachtwagens en bedrijfsvoertuigen",
                "fr": "SSTP - Services d'informations concernant les aires de stationnement sûres et sécurisées pour les camions et les véhicules commerciaux",
                "de": "SSTP - Informationdiensten für sichere Parkplätze für Lastkraftwagen und andere gewerbliche Fahrzeuge"
            })
        ]

MOBILITY_THEME = [
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/air-and-space-travel", {
            "en": "Air and space travel",
            "nl": "Lucht- en ruimtevaart",
            "fr": "Transport aérien et spatial",
            "de": "Luft- und Raumfahrt"
        })
    ],
    []),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/cycle-network-data", {
            "en": "Cycle network data",
            "nl": "Fietsnetwerk informatie",
            "fr": "Données sur le réseau cyclable",
            "de": "Daten zum Fahrradnetzwerk"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/network-closures-diversions", {
            "en": "Network closures/diversions",
            "nl": "Fietsroutenetwerk afsluitingen/omleidingen",
            "fr": "Fermetures/déviations du réseau",
            "de": "Netzsperrungen/Umleitungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/network-detailed-attributes", {
            "en": "Network detailed attributes",
            "nl": "Exacte kenmerken fietsroutenetwerk",
            "fr": "Caractéristiques des réseaux cyclables",
            "de": "Ausführliche Angaben zum Radwegenetz"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/network-geometry-and-lane-character", {
            "en": "Network geometry and lane character",
            "nl": "Fietsnetwerk geometrie en karakter",
            "fr": "Géométrie du réseau et caractéristiques des voies",
            "de": "Netzgeometrie und Fahrbahnbeschaffenheit"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/dynamic-traffic-signs-and-regulations", {
            "en": "Dynamic traffic signs and regulations",
            "nl": "Dynamische verkeerssignalisatie en verkeersregels",
            "fr": "Panneaux routiers et réglementations dynamiques",
            "de": "Dynamische Verkehrszeichen und -regelungen"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/bridge-closures-and-access-conditions", {
            "en": "Bridge closures and access conditions",
            "nl": "Sluitings- en toegangsvoorwaarden voor bruggen",
            "fr": "Fermetures de ponts et conditions d'accès",
            "de": "Brückensperrungen und Zufahrtsbedingungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/direction-of-travel-on-reversible-lanes", {
            "en": "Direction of travel on reversible lanes",
            "nl": "Rijrichting van rijstroken met omkeerbare rijrichting",
            "fr": "Sens de la circulation sur les voies réversibles",
            "de": "Fahrtrichtung auf Fahrbahnen für beide Richtungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/dynamic-overtaking-bans-on-heavy-goods-vehicles", {
            "en": "Dynamic overtaking bans on heavy goods vehicles",
            "nl": "Dynamische inhaalverboden voor vrachtwagens",
            "fr": "Interdictions dynamiques de dépassement pour les poids lourds",
            "de": "Dynamische Überholverbote für schwere Nutzfahrzeuge"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/dynamic-speed-limits", {
            "en": "Dynamic speed limits",
            "nl": "Dynamische snelheidsbeperkingen",
            "fr": "Limitations de vitesse dynamiques",
            "de": "Dynamische Geschwindigkeitsbegrenzungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/lane-closures-and-access-conditions", {
            "en": "Lane closures and access conditions",
            "nl": "Sluitings- en toegangsvoorwaarden voor rijstroken",
            "fr": "Fermetures de voies et conditions d'accès",
            "de": "Fahrstreifensperrungen und Zufahrtsbedingungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/other-access-restrictions-and-traffic-regulations", {
            "en": "Other access restrictions and traffic regulations",
            "nl": "Andere toegangsbeperkingen en verkeersregelingen",
            "fr": "Autres restrictions d'accès et règles de circulation",
            "de": "Sonstige Zufahrtsbeschränkungen und Straßenverkehrsvorschriften"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/other-temporary-traffic-management-measures-or-plans", {
            "en": "Other temporary traffic management measures or plans",
            "nl": "Andere tijdelijke verkeerbeheersmaatregelen of -plannen",
            "fr": "Autres mesures ou plans temporaires de gestion de la circulation",
            "de": "Sonstige befristete Verkehrsmanagementmaßnahmen oder -pläne"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/road-closures-and-access-conditions", {
            "en": "Road closures and access conditions",
            "nl": "Sluitings- en toegangsvoorwaarden voor wegen",
            "fr": "Fermetures de routes et conditions d'accès",
            "de": "Straßensperrungen und Zufahrtsbedingungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/tunnel-closures-and-access-conditions", {
            "en": "Tunnel closures and access conditions",
            "nl": "Sluitings- en toegangsvoorwaarden voor tunnels",
            "fr": "Fermetures de tunnels et conditions d'accès",
            "de": "Tunnelsperrungen und Zufahrtsbedingungen"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/filling-and-charging-stations", {
            "en": "Filling and charging stations",
            "nl": "Tankstations en laadpunten",
            "fr": "Stations-services et de recharge",
            "de": "Tankstellen und Ladestationen"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/availability-of-charging-points-for-electric-vehicles", {
            "en": "Availability of charging points for electric vehicles",
            "nl": "Beschikbaarheid laadpunten elektrische voertuigen",
            "fr": "Disponibilité des points de recharge pour véhicules électriques",
            "de": "Verfügbarkeit von Ladepunkten für Elektrofahrzeuge"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/availability-of-filling-stations", {
            "en": "Availability of filling stations",
            "nl": "Beschikbaarheid tankstations",
            "fr": "Disponibilité des stations de ravitaillement",
            "de": "Verfügbarkeit von Tankstellen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/location-and-conditions-of-charging-points", {
            "en": "Location and conditions of charging points",
            "nl": "Locatie en gebruiksvoorwaarden laadpunten elektrische voertuigen",
            "fr": "Localisation des points de recharge et conditions de leur utilisation",
            "de": "Standort von Ladestationen und ihre Nutzungsbedingungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/location-and-conditions-of-filling-stations", {
            "en": "Location and conditions of filling stations",
            "nl": "Locatie en gebruiksvoorwaarden tankstations",
            "fr": "Localisation des stations de ravitaillement et conditions de leur utilisation",
            "de": "Standort von Tankstellen und ihre Nutzungsbedingungen"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/freight-and-logistics", {
            "en": "Freight and logistics",
            "nl": "Goederen en logistiek",
            "fr": "Marchandises et logistique",
            "de": "Waren und Logistik"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/availability-of-delivery-areas", {
            "en": "Availability of delivery areas",
            "nl": "Beschikbaarheid leverzones",
            "fr": "Disponibilité des zones de livraison",
            "de": "Verfügbarkeit von Lieferzonen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/freight-delivery-regulations", {
            "en": "Freight delivery regulations",
            "nl": "Regels voor het leveren van goederen",
            "fr": "Réglementations sur la livraison de fret",
            "de": "Lieferverkehrsbestimmungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/location-of-delivery-areas", {
            "en": "Location of delivery areas",
            "nl": "Locatie leverzones",
            "fr": "Localisation des zones de livraison",
            "de": "Standort von Lieferzonen"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/general-information-for-trip-planning", {
            "en": "General information for trip-planning",
            "nl": "Algemene informatie voor routeplanning",
            "fr": "Informations générales pour la planification des déplacements",
            "de": "Allgemeine Informationen zu Routenplanung"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/address-identifiers", {
            "en": "Address identifiers",
            "nl": "Adresgegevens",
            "fr": "Adresses",
            "de": "Adressen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/parameters-needed-to-calculate-costs", {
            "en": "Parameters needed to calculate costs",
            "nl": "Parameters voor berekening kosten",
            "fr": "Paramètres nécessaires pour calculer des coûts",
            "de": "Parameter zur Berechnung von Kosten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/parameters-needed-to-calculate-environmental-factors", {
            "en": "Parameters needed to calculate environmental factors",
            "nl": "Parameters voor berekening milieueffecten",
            "fr": "Paramètres nécessaires pour calculer un facteur environnemental",
            "de": "Parameter zur Berechnung von Umweltfaktoren"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/points-of-interest", {
            "en": "Points of interest",
            "nl": "POI's (interessante plaatsen i.k.v. reizen)",
            "fr": "Points d'intérêt",
            "de": "Orte von Interesse"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/topographic-places", {
            "en": "Topographic places",
            "nl": "Topografische gegevens",
            "fr": "Lieux topographiques",
            "de": "Topografische Orte"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/other", {
            "en": "Other",
            "nl": "Andere",
            "fr": "Autres",
            "de": "Anderen"
        })
    ],
     []),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/parking-service-and-rest-area-information", {
            "en": "Parking, service and rest area information",
            "nl": "Parking en stopplaatsen informatie",
            "fr": "Informations sur les aires de stationnement et de repos",
            "de": "Informationen zu Park- und Rastplätzen"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/bike-parking-locations", {
            "en": "Bike-parking locations",
            "nl": "Fietsenstallingen",
            "fr": "Stationnements pour vélos",
            "de": "Fahrradstellplätze"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/car-parking-availability", {
            "en": "Car parking availability",
            "nl": "Beschikbaarheid parkeerplaatsen",
            "fr": "Places de parking disponibles",
            "de": "Verfügbare Pkw-Parkplätze"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/car-parking-locations-and-conditions", {
            "en": "Car parking locations and conditions",
            "nl": "Locatie en voorwaarden parkeerterreinen",
            "fr": "Localisation et conditions des parkings",
            "de": "Standort und Bedingungen von Pkw-Parkplätze"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/park-and-ride-stops", {
            "en": "Park and ride stops",
            "nl": "Park&Ride-haltes",
            "fr": "Parkings de délestage",
            "de": "\"Park & Ride\"-Standorte"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/service-and-rest-area-availability", {
            "en": "Service and rest area availability",
            "nl": "Beschikbaarheid service- en stopplaatsen",
            "fr": "Disponibilité des aires de service et de repos",
            "de": "Verfügbarkeit von sicheren Parkplätzen und Rastanlagen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/service-and-rest-area-locations-and-conditions", {
            "en": "Service and rest area locations and conditions",
            "nl": "Locatie en voorwaarden van service- en stopplaatsen",
            "fr": "Localisation et conditions des aires de service et de repos",
            "de": "Standort und Bedingungen von sicheren Parkplätzen und Rastanlagen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/truck-parking-availability", {
            "en": "Truck parking availability",
            "nl": "Beschikbaarheid parkeerplaatsen voor vrachtwagens",
            "fr": "Disponibilité des aires de stationnement pour camions",
            "de": "Verfügbarkeit von Lkw-Parkplatzes"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/truck-parking-locations-and-conditions", {
            "en": "Truck parking locations and conditions",
            "nl": "Locatie en voorwaarden parkeerplaatsen voor vrachtwagens",
            "fr": "Localisation et conditions des aires de stationnement pour camions",
            "de": "Standort und Bedingungen von Pkw-Parkplätze"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/pedestrian-network-data", {
            "en": "Pedestrian network data",
            "nl": "Voetgangersnetwerk informatie",
            "fr": "Données sur le réseau piétonnier",
            "de": "Fußwegenetz"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/pedestrian-accessibility-facilities", {
            "en": "Pedestrian accessibility facilities",
            "nl": "Toegankelijkheidsfaciliteiten voetgangers",
            "fr": "Aménagements pour l'accessibilité des piétons",
            "de": "Zugänglichkeitshilfen für Fußgänger"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/pedestrian-network-geometry", {
            "en": "Pedestrian network geometry",
            "nl": "Geometrie voetgangersnetwerk",
            "fr": "Géométrie du réseau piétonnier",
            "de": "Geometrie des Fußgängernetzes"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/public-transport-non-scheduled-transport", {
            "en": "Non-scheduled public transport",
            "nl": "Ongeregeld openbaar vervoer",
            "fr": "Transports publics non réguliers",
            "de": "Öffentlicher Nicht-Linienverkehr"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/accesibility-information-for-vehicles", {
            "en": "Accesibility information for vehicles",
            "nl": "Toegankelijkheid voertuigen",
            "fr": "Informations sur l'accessibilité des véhicules",
            "de": "Zugänglichkeitsinformationen für Fahrzeuge"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/environmental-standards-for-vehicles", {
            "en": "Environmental standards for vehicles",
            "nl": "Milieuparameters voertuigen",
            "fr": "Normes environnementales pour les véhicules",
            "de": "Umweltstandards für Fahrzeuge"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/fares", {
            "en": "Fares",
            "nl": "Tarieven",
            "fr": "Tarifs",
            "de": "Tarifen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/locations-and-stations", {
            "en": "Locations and stations",
            "nl": "Locaties en haltes",
            "fr": "Localisations et stations",
            "de": "Standorte und Stellplätze"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/provider-data", {
            "en": "Provider data",
            "nl": "Informatie dienstverlener",
            "fr": "Données des prestataires",
            "de": "Anbieterdaten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/reservation-and-purchase-options", {
            "en": "Reservation and purchase options",
            "nl": "Reservatie en aankoop mogelijkheden",
            "fr": "Modalités de réservation et d'achat",
            "de": "Reservierungs- und Kaufmöglichkeiten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/service-areas-and-service-times", {
            "en": "Service areas and service times",
            "nl": "Locatie en bedrijfsuren diensten",
            "fr": "Zones desservies et horaires de service",
            "de": "Einzugsgebiete und Dienstzeiten"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/public-transport-scheduled-transport", {
            "en": "Scheduled public transport",
            "nl": "Geregeld openbaar vervoer",
            "fr": "Transports publics réguliers",
            "de": "Öffentlicher Linienverkehr"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/basic-commercial-conditions", {
            "en": "Basic commercial conditions",
            "nl": "Belangrijkste commerciële voorwaarden",
            "fr": "Conditions commerciales de base",
            "de": "Grundlegende Geschäftsbedingungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/basic-common-standard-fares", {
            "en": "Basic common standard fares",
            "nl": "Algemene basistarieven",
            "fr": "Tarifs standards communs de base",
            "de": "Grunddaten zu normalen Standardtarifen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/common-fare-products", {
            "en": "Common fare products",
            "nl": "Gemeenschappelijke tariefformules",
            "fr": "Produits tarifaires communs",
            "de": "Normaltarifprodukte"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/connection-links", {
            "en": "Connection links",
            "nl": "Knooppunten waar kan worden overgestapt",
            "fr": "Points d’échange avec possibilité de correspondances",
            "de": "Anschlussverbindungen an Verkehrsknotenpunkten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/disruptions-delays-cancellations", {
            "en": "Disruptions, delays, cancellations",
            "nl": "Storingen, vertragingen, uitval",
            "fr": "Perturbations, retards, annulations",
            "de": "Störungen, Verspätungen, Ausfälle"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/environmental-standards-for-vehicles", {
            "en": "Environmental standards for vehicles",
            "nl": "Milieuparameters voertuigen",
            "fr": "Normes environnementales pour les véhicules",
            "de": "Umweltstandards für Fahrzeuge"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/hours-of-operation", {
            "en": "Hours of operation",
            "nl": "Bedrijfsuren",
            "fr": "Horaires d'exploitation",
            "de": "Betriebszeiten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/network-topology-and-routes-lines", {
            "en": "Network topology and routes/lines",
            "nl": "Netwerktopologie en -routes/lijnen",
            "fr": "Topologie du réseau et itinéraires/lignes",
            "de": "Netztopologie und Routen/Strecken"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/operational-calendar", {
            "en": "Operational Calendar",
            "nl": "Exploitatieplanning",
            "fr": "Calendrier opérationnel",
            "de": "Betriebskalender"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/passenger-classes", {
            "en": "Passenger classes",
            "nl": "Passagiersklassen",
            "fr": "Catégories de voyageurs",
            "de": "Kategorien von Verkehrsdienstnutzern"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/planned-interchanges-between-scheduled-services", {
            "en": "Planned interchanges between scheduled services",
            "nl": "Geplande overstappen tussen geregeld vervoer",
            "fr": "Correspondances planifiées entre services réguliers",
            "de": "Planmäßiges Umsteigen zwischen Linienverkehrsdiensten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/purchase-information", {
            "en": "Purchase information",
            "nl": "Verkoopinformatie",
            "fr": "Information sur les achats",
            "de": "Kaufinformationen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/real-time-estimated-departure-and-arrival-times", {
            "en": "Real-time estimated departure and arrival times",
            "nl": "Real-time geraamde vertrek- en aankomsttijden",
            "fr": "Heures de départ et d’arrivée estimées en temps réel",
            "de": "Geschätzte Abfahrts- und Ankunftszeiten in Echtzeit"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/special-fare-products", {
            "en": "Special Fare Products",
            "nl": "Speciale aanbiedingen",
            "fr": "Produits tarifaires spéciaux",
            "de": "Sondertarifprodukte"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/stop-facilities-accessibility-and-paths-within-facility", {
            "en": "Stop facilities accessibility and paths within facility",
            "nl": "Toegankelijkheid van knooppunten en routes binnen knooppunten",
            "fr": "Accessibilité des points d'arrêt et voies de circulation au sein d'un point d'échange",
            "de": "Zugänglichkeit von Zugangsknoten und Wege innerhalb von Verkehrsknotenpunkten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/stop-facilities-geometry-and-map-layout", {
            "en": "Stop facilities geometry and map layout",
            "nl": "Geometrie/situering van de knooppunten op kaart",
            "fr": "Géométrie/structure de la carte des nœuds d'accès",
            "de": "Geometrie/Kartierung von Zugangsknoten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/stop-facilities-location-and-features", {
            "en": "Stop facilities location and features",
            "nl": "Locatie en toegangen tot het knooppunt",
            "fr": "Localisation et situation aux nœuds d'accès",
            "de": "Standort und Angaben von Zugangsknoten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/stop-facilities-status-of-features", {
            "en": "Stop facilities status of features",
            "nl": "Status van de toegangen tot het knooppunt",
            "fr": "Situation aux nœuds d'accès",
            "de": "Statusangaben für Zugangsknoten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/timetables-static", {
            "en": "Timetables static",
            "nl": "Dienstregelingen statisch",
            "fr": "Horaires statiques",
            "de": "Fahrpläne statisch"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/transport-operators", {
            "en": "Transport operators",
            "nl": "Transport operator",
            "fr": "Exploitants d'entreprises de transport",
            "de": "Verkehrsbetreiber"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/vehicle-details", {
            "en": "Vehicle details",
            "nl": "Voertuig details",
            "fr": "Détails du véhicule",
            "de": "Fahrzeugdetails"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/real-time-traffic-data", {
            "en": "Real-time traffic data",
            "nl": "Real-time verkeersinformatie",
            "fr": "Données en temps réel sur la circulation",
            "de": "Echtzeit-Verkehrsinformation"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/current-travel-times", {
            "en": "Current travel times",
            "nl": "Huidige reistijd",
            "fr": "Temps de parcours actuels",
            "de": "Aktuelle Reisezeiten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/expected-delays", {
            "en": "Expected delays",
            "nl": "Verwachte vertragingen",
            "fr": "Retards prévus",
            "de": "Erwartete Verspätungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/location-and-length-of-queues", {
            "en": "Location and length of queues",
            "nl": "Plaats en lengte van files",
            "fr": "Localisation et longueur des embouteillages",
            "de": "Lage und Länge von Verkehrsstaus"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/predicted-travel-times", {
            "en": "Predicted travel times",
            "nl": "Voorspelde reistijd",
            "fr": "Temps de parcours prévus",
            "de": "Voraussichtliche Reisezeiten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/speed", {
            "en": "Speed",
            "nl": "Snelheid",
            "fr": "Vitesse",
            "de": "Geschwindigkeit"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/traffic-data-at-border-crossings-to-third-countries", {
            "en": "Traffic data at border crossings to third countries",
            "nl": "Verkeersdata bij grensovergangen naar derde landen",
            "fr": "Données sur le trafic aux frontières avec les pays tiers",
            "de": "Verkehrsdaten an Grenzübergängen zu Drittländern"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/traffic-volume", {
            "en": "Traffic volume",
            "nl": "Verkeersvolume",
            "fr": "Volume du traffic",
            "de": "Verkehrsaufkommen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/waiting-time-at-border-crossings-to-non-eu-member-states", {
            "en": "Waiting time at border crossings to non-EU member states",
            "nl": "Wachttijd bij grensovergangen naar niet EU-landen",
            "fr": "Temps d’attente aux frontières des pays non membres de l'UE",
            "de": "Wartezeit an Grenzübergängen zu Nicht-EU-Mitgliedstaaten"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/road-events-and-conditions", {
            "en": "Road events and conditions",
            "nl": "Wegenincidenten en condities",
            "fr": "Événements et conditions de route",
            "de": "Straßeneignisse und –zustände"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/accidents-and-incidents", {
            "en": "Accidents and incidents",
            "nl": "Ongevallen en incidenten",
            "fr": "Accidents et incidents",
            "de": "Unfälle und Störungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/poor-road-conditions", {
            "en": "Poor road conditions",
            "nl": "Slechte wegentoestanden",
            "fr": "État dégradé de la chaussée",
            "de": "Schlechter Straßenzustand"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/road-weather-conditions", {
            "en": "Road weather conditions",
            "nl": "Weercondities wegen",
            "fr": "Conditions météorologiques routières",
            "de": "Straßenwetterszustände"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/road-work-information", {
            "en": "Road work information",
            "nl": "Wegenwerken informatie",
            "fr": "Informations sur les travaux routiers",
            "de": "Informationen zu Straßenbauarbeiten"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/long-term-road-works", {
            "en": "Long-term road works",
            "nl": "Langetermijn wegenwerken",
            "fr": "Travaux routiers de longue durée",
            "de": "Langfristige Straßenbauarbeiten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/short-term-road-works", {
            "en": "Short-term road works",
            "nl": "Kortetermijn wegenwerken",
            "fr": "Travaux routiers de courte durée",
            "de": "Kurzfristige Straßenbauarbeiten"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/sharing-and-hiring-services", {
            "en": "Sharing and Hiring Services",
            "nl": "Deel- en huurdiensten",
            "fr": "Services de partage et de location",
            "de": "Gemeinsame Nutzung und Vermietung von Dienstleistungen"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/bike-hiring-availability", {
            "en": "Bike-hiring availability",
            "nl": "Beschikbaarheid huurfietsen",
            "fr": "Disponibilité de vélos en libre service",
            "de": "Verfügbarkeit von Leihfahrrädern"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/bike-hiring-stations", {
            "en": "Bike-hiring stations",
            "nl": "Standplaatsen fietsverhuur",
            "fr": "Stations de vélos en libre service",
            "de": "Stellplätze für Leihfahrrädern"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/bike-sharing-availability", {
            "en": "Bike sharing availability",
            "nl": "Beschikbaarheid deelfietsen",
            "fr": "Disponibilité des vélos partagés",
            "de": "Verfügbarkeit von gemeinsam genutzter Fahrräder (Bike-sharing)"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/bike-sharing-locations-and-stations", {
            "en": "Bike sharing locations and stations",
            "nl": "Locatie en standplaatsen deelfietsen",
            "fr": "Localisation et stations de vélos partagés",
            "de": "Standorte und Stellplätze für gemeinsam genutzte Fahrräder (Bike-sharing)"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/car-hiring-availability", {
            "en": "Car-hiring availability",
            "nl": "Beschikbaarheid huurauto’s",
            "fr": "Disponibilité des locations de voiture",
            "de": "Verfügbarkeit von Mietwagen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/car-hiring-stations", {
            "en": "Car-hiring stations",
            "nl": "Standplaatsen huurauto’s",
            "fr": "Stations de location de voitures",
            "de": "Stellplätze für Mietwagen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/car-sharing-availability", {
            "en": "Car-sharing availability",
            "nl": "Beschikbaarheid deelauto's",
            "fr": "Disponibilité des voitures partagées",
            "de": "Verfügbarkeit gemeinsam genutzter Pkw (Car-sharing)"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/car-sharing-locations-and-stations", {
            "en": "Car-sharing locations and stations",
            "nl": "Locatie en standplaatsen deelauto's",
            "fr": "Localisation et stations de voitures partagées",
            "de": "Standorte und Stellplätze für gemeinsam genutzter Pkw (Car-Sharing)"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/environmental-standards-for-vehicles", {
            "en": "Environmental standards for vehicles",
            "nl": "Milieuparameters voertuigen",
            "fr": "Normes environnementales pour les véhicules",
            "de": "Umweltstandards für Fahrzeuge"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/e-scooter-sharing-availability", {
            "en": "E-scooter sharing availability",
            "nl": "Beschikbaarheid deelscooters",
            "fr": "Disponibilité des trottinettes électriques partagées",
            "de": "Verfügbarkeit gemeinsam genutzter E-Roller (E-scooter sharing)"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/e-scooter-sharing-locations-and-stations", {
            "en": "E-scooter sharing locations and stations",
            "nl": "Locatie en standplaatsen deelscooters",
            "fr": "Localisation et stations de trottinettes électriques partagées",
            "de": "Standorte und Stellplätze für gemeinsam genutzter E-Roller (E-scooter sharing)"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/payment-methods", {
            "en": "Payment methods",
            "nl": "Betaalmethoden",
            "fr": "Modes de paiement",
            "de": "Zahlungsmöglichkeiten"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/static-road-network-data", {
            "en": "Static road network data",
            "nl": "Statische weggegevens",
            "fr": "Données routières statiques",
            "de": "Statische Straβendaten"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/geometry", {
            "en": "Geometry",
            "nl": "Geometrie",
            "fr": "Géométrie",
            "de": "Geometrie"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/gradients", {
            "en": "Gradients",
            "nl": "Hellingen",
            "fr": "Pentes",
            "de": "Steigungen/Gefälle"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/junctions", {
            "en": "Junctions",
            "nl": "Knooppunten",
            "fr": "Jonctions",
            "de": "Kreuzungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/number-of-lanes", {
            "en": "Number of lanes",
            "nl": "Aantal rijstroken",
            "fr": "Nombre de voies",
            "de": "Anzahl der Fahrstreifen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/road-classification", {
            "en": "Road classification",
            "nl": "Wegclassificatie",
            "fr": "Classification de la route",
            "de": "Straßenklasse"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/road-width", {
            "en": "Road width",
            "nl": "Breedte van de weg",
            "fr": "Largeur de la route",
            "de": "Straßenbreite"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/static-traffic-signs-and-regulations", {
            "en": "Static traffic signs and regulations",
            "nl": "Statische verkeerssignalisatie en verkeersregels",
            "fr": "Panneaux routiers et réglementations statiques",
            "de": "Statische Verkehrszeichen und -regelungen"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/bridge-access-conditions", {
            "en": "Bridge access conditions",
            "nl": "Toegangsvoorwaarden voor bruggen",
            "fr": "Conditions d'accès aux ponts",
            "de": "Zufahrtsbedingungen für Brücken"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/other-static-traffic-signs", {
            "en": "Other static traffic signs",
            "nl": "Andere statische verkeersborden",
            "fr": "Autres panneaux de signalisation statique",
            "de": "Sonstige statische Verkehrszeichen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/other-traffic-regulations", {
            "en": "Other traffic regulations",
            "nl": "Andere verkeersregelingen",
            "fr": "Autres règles de circulation",
            "de": "Sonstige Straßenverkehrsvorschriften"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/permanent-access-restrictions", {
            "en": "Permanent access restrictions",
            "nl": "Permanente toegangsbeperkingen",
            "fr": "Restrictions d'accès permanentes",
            "de": "Dauerhafte Zufahrtsbeschränkungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/speed-limits", {
            "en": "Speed limits",
            "nl": "Snelheidsbeperkingen",
            "fr": "Limitations de vitesse",
            "de": "Schnellheitsbegrenzungen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/traffic-circulation-plans", {
            "en": "Traffic circulation plans",
            "nl": "Verkeerscirculatieplannen",
            "fr": "Plans de circulation routière",
            "de": "Verkehrspläne"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/tunnel-access-conditions", {
            "en": "Tunnel access conditions",
            "nl": "Toegangsvoorwaarden voor tunnels",
            "fr": "Conditions d'accès aux tunnels",
            "de": "Zufahrtsbedingungen für Tunnel"
        })
    ]),
    ([
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/toll-information", {
            "en": "Toll information",
            "nl": "Tol informatie",
            "fr": "Informations sur les péages",
            "de": "Mautangaben"
        })
    ], [
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/applicable-road-user-charges-and-payment-methods", {
            "en": "Applicable road user charges and payment methods",
            "nl": "Heffingen van toepassing voor weggebruikers en betaalmethoden",
            "fr": "Redevances fixes applicables aux usagers de la route et modes de paiement",
            "de": "Geltende Benutzungsgebühren und Zahlungsmöglichkeiten"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/identification-of-tolled-roads", {
            "en": "Identification of tolled roads",
            "nl": "Identificatie van tolwegen",
            "fr": "Identification des routes à péage",
            "de": "Ausweisung von Mautstraßen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/location-of-tolling-stations", {
            "en": "Location of tolling stations",
            "nl": "Locatie tolstations",
            "fr": "Localisation des postes de péage",
            "de": "Standort der Mautstationen"
        }),
        ("https://w3id.org/mobilitydcat-ap/mobility-theme/payment-methods-for-tolls", {
            "en": "Payment methods for tolls",
            "nl": "Betaalmethoden tolstations",
            "fr": "Modes de paiement aux péages",
            "de": "Zahlungsmöglichkeiten für die Maut"
        })
    ]),
    ([
         ("https://w3id.org/mobilitydcat-ap/mobility-theme/waterways-and-water-bodies", {
             "en": "Waterways and water-bodies",
             "nl": "Zee en binnenwateren",
             "fr": "Voies navigables et plans d'eau",
             "de": "Wasserstraßen und Wasserkörper"
         })
     ],
     [])
]

LICENSE_TYPE = LICENSE_TYPE_CONCEPTS.copy()
LICENSE_TYPE.append(
    ('Other', {
        "en": "Other",
        "fr": "Autre",
        "nl": "Andere",
        "de": "Andere"
    }))

ENCODING = [
    ('US-ASCII', {
        "en": "ASCII",
        "fr": "ASCII",
        "nl": "ASCII",
        "de": "ASCII"
    }),
    ('UTF-8', {
        "en": "UTF-8",
        "fr": "UTF-8",
        "nl": "UTF-8",
        "de": "UTF-8"
    }),
    ('UTF-16', {
        "en": "UTF-16",
        "fr": "UTF-16",
        "nl": "UTF-16",
        "de": "UTF-16"
    }),
    ('ISO-8859-1', {
        "en": "ISO-8859-1",
        "fr": "ISO-8859-1",
        "nl": "ISO-8859-1",
        "de": "ISO-8859-1"
    }),
    ('ISO-8859-15', {
        "en": "ISO-8859-15",
        "fr": "ISO-8859-15",
        "nl": "ISO-8859-15",
        "de": "ISO-8859-15"
    }),
    ('Other', {
       "en": "Other",
        "fr": "Autre",
        "nl": "Andere",
        "de": "Andere"
    })
]



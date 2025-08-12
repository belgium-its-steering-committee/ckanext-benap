
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

NAP_TYPE = [
    ('MMTIS', {
        "en": "MMTIS - Multimodal travel information services", "nl": "MMTIS - Multimodale reisinformatiediensten", "fr": "MMTIS - Services d'informations sur les déplacements multimodaux",
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

MOBILITY_DATASET_TYPE = [
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

from ckanext.benap.constants.concept_collections.mobilitydcat.transport_mode import DEMAND_RESPONSIVE, OTHER, PERSONAL, SCHEDULED

BY_CATEGORY = [
    (SCHEDULED, {
            "en": "Scheduled",
            "nl": "Openbaar vervoer",
            "fr": "Services réguliers",
            "de": "Linienverkehrsdienste"
        }),
    (DEMAND_RESPONSIVE, {
            "en": "Demand-responsive",
            "nl": "Aanbod afhankelijke inzet",
            "fr": "Services à la demande",
            "de": "Abruf-Verkehrsdienste"
        }),
    (PERSONAL, {
            "en": "Personal",
            "nl": "Persoonlijk vervoer",
            "fr": "Modes personnels",
            "de": "Individualverkehr"
        }),
    (OTHER, {
            "en": "Not applicable",
            "nl": "Niet toepasbaar",
            "fr": "Non applicable",
            "de": "Nicht anwendbar"
        }
    )
]

import ckanext.benap.constants.concept_collections.mobilitydcat.mobility_theme as mt

MOBILITY_THEME_BROADER_NARROWER_MAPPING = (
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/air-and-space-travel",
        None),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/cycle-network-data",
        mt.CYCLE_NETWORK_DATA.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/dynamic-traffic-signs-and-regulations",
        mt.DYNAMIC_TRAFFIC_SIGNS_AND_REGULATIONS.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/filling-and-charging-stations",
        mt.FILLING_AND_CHARGING_STATIONS.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/freight-and-logistics",
        mt.FREIGHT_AND_LOGISTICS.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/general-information-for-trip-planning",
        mt.GENERAL_INFORMATION_FOR_TRIP_PLANNING.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/other",
        None),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/parking-service-and-rest-area-information",
        mt.PARKING_AREA_AND_REST_SERVICE_INFORMATION.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/pedestrian-network-data",
        mt.PEDESTRIAN_NETWORK_DATA.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/public-transport-non-scheduled-transport",
        mt.PUBLIC_TRANSPORT_NON_SCHEDULED_TRANSPORT.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/public-transport-scheduled-transport",
        mt.PUBLIC_TRANSPORT_SCHEDULED_TRANSPORT.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/real-time-traffic-data",
        mt.REAL_TIME_TRAFFIC_DATA.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/road-events-and-conditions",
        mt.ROAD_EVENTS_AND_CONDITIONS.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/road-work-information",
        mt.ROAD_WORK_INFORMATION.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/sharing-and-hiring-services",
        mt.SHARING_AND_HIRING_SERVICES.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/static-road-network-data",
        mt.STATIC_AND_ROAD_NETWORK_DATA.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/static-traffic-signs-and-regulations",
        mt.STATIC_TRAFFIC_SIGNS_AND_REGULATIONS.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/toll-information",
        mt.TOLL_INFORMATION.items()),
    ("https://w3id.org/mobilitydcat-ap/mobility-theme/waterways-and-water-bodies",
        None)
)

# Build structure expected by form logic for hierarchical concept-scheme-like forms
MOBILITY_THEME = []
for broader_uri, narrower_collection in MOBILITY_THEME_BROADER_NARROWER_MAPPING:
    if narrower_collection:
        narrower = narrower_collection
    else:
        narrower = []

    broader_narrower = tuple([[tuple([broader_uri, mt.MOBILITY_THEME_BROADER[broader_uri]])], narrower])
    MOBILITY_THEME.append(broader_narrower)

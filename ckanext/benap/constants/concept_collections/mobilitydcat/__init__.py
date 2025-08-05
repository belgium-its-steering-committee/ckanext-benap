#!/usr/bin/env python3
from collections import OrderedDict

from . import (application_layer_protocol,
               communication_method,
               conditions_access_usage,
               georeferencing_method,
               grammar,
               mobility_data_standard,
               network_coverage,
               transport_mode,
               mobility_theme as mt)

APPLICATION_LAYER_PROTOCOL = OrderedDict(application_layer_protocol.APPLICATION_LAYER_PROTOCOL)
COMMUNICATION_METHOD = OrderedDict(communication_method.COMMUNICATION_METHOD)
CONDITIONS_ACCESS_USAGE = OrderedDict(conditions_access_usage.ACCESS + conditions_access_usage.USAGE)
GEOREFERENCING_METHOD = OrderedDict(georeferencing_method.GEOREFERENCING_METHOD)
GRAMMAR = OrderedDict(grammar.GRAMMAR)
MOBILITY_DATA_STANDARD = OrderedDict(mobility_data_standard.MOBILITY_DATA_STANDARD)
NETWORK_COVERAGE = OrderedDict(network_coverage.NETWORK_COVERAGE)
TRANSPORT_MODE = OrderedDict(transport_mode.DEMAND_RESPONSIVE + transport_mode.PERSONAL + transport_mode.SCHEDULED + transport_mode.OTHER)
MOBILITY_THEME = {**mt.CYCLE_NETWORK_DATA,
                  **mt.DYNAMIC_TRAFFIC_SIGNS_AND_REGULATIONS,
                  **mt.FILLING_AND_CHARGING_STATIONS,
                  **mt.FREIGHT_AND_LOGISTICS,
                  **mt.GENERAL_INFORMATION_FOR_TRIP_PLANNING,
                  **mt.MOBILITY_THEME_BROADER,
                  **mt.PARKING_AREA_AND_REST_SERVICE_INFORMATION,
                  **mt.PEDESTRIAN_NETWORK_DATA,
                  **mt.PUBLIC_TRANSPORT_NON_SCHEDULED_TRANSPORT,
                  **mt.PUBLIC_TRANSPORT_SCHEDULED_TRANSPORT,
                  **mt.REAL_TIME_TRAFFIC_DATA,
                  **mt.ROAD_EVENTS_AND_CONDITIONS,
                  **mt.ROAD_WORK_INFORMATION,
                  **mt.SHARING_AND_HIRING_SERVICES,
                  **mt.STATIC_AND_ROAD_NETWORK_DATA,
                  **mt.STATIC_TRAFFIC_SIGNS_AND_REGULATIONS,
                  **mt.TOLL_INFORMATION}


CONCEPTS = {**APPLICATION_LAYER_PROTOCOL,
            **COMMUNICATION_METHOD,
            **CONDITIONS_ACCESS_USAGE,
            **GEOREFERENCING_METHOD,
            **GRAMMAR,
            **MOBILITY_DATA_STANDARD,
            **NETWORK_COVERAGE,
            **TRANSPORT_MODE,
            **MOBILITY_THEME}

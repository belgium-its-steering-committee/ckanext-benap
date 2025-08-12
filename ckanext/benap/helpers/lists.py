# coding=utf-8
# NOTE: Even if below imports seem no longer imported literally elsewhere,
# they still might be in use by `benap_retrieve_raw_choices_list`
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
from ckanext.benap.constants.codelists import ENCODING, NAP_TYPE, MOBILITY_DATASET_TYPE as DATASET_TYPE
from ckanext.benap.constants.mobility_theme_form import MOBILITY_THEME

LICENSE_TYPE = LICENSE_TYPE_CONCEPTS.copy()
LICENSE_TYPE.append(
    ('Other', {
        "en": "Other",
        "fr": "Autre",
        "nl": "Andere",
        "de": "Andere"
    }))

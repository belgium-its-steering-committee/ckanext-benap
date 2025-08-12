#!/usr/bin/env python3
from collections import OrderedDict

from .eu_authority import CONCEPTS as EU_CONCEPTS
from .mobilitydcat import CONCEPTS as MOBILITYDCAT_CONCEPTS
from .nuts import CONCEPTS as NUTS_CONCEPTS
from .opengis_crs import REFERENCE_SYSTEM as OPENGIS_CRS

CONCEPTS = {
    **EU_CONCEPTS,
    **MOBILITYDCAT_CONCEPTS,
    **NUTS_CONCEPTS,
    **dict(OPENGIS_CRS),
}

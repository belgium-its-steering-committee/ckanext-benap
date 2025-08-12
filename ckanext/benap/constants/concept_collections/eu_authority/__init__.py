#!/usr/bin/env python3
from collections import OrderedDict

from . import (country,
               file_type,
               frequency,
               license_type)

EU_COUNTRIES = OrderedDict(country.EU_COUNTRIES)
FILE_TYPE = OrderedDict(file_type.FILE_TYPE)
FREQUENCY = OrderedDict(frequency.FREQUENCY)
LICENSE_TYPE = OrderedDict(license_type.LICENSE_TYPE)

CONCEPTS = {**EU_COUNTRIES,
            **FILE_TYPE,
            **FREQUENCY,
            **LICENSE_TYPE}

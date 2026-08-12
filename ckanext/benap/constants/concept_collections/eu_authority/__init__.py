#!/usr/bin/env python3
from collections import OrderedDict

from . import (country,
               file_type,
               frequency,
               license_type)

EU_COUNTRIES = OrderedDict(country.EU_COUNTRIES)
FILE_TYPE = OrderedDict(t[0:2] for t in file_type.FILE_TYPE)
FREQUENCY = OrderedDict(t[0:2] for t in frequency.FREQUENCY)
LICENSE_TYPE = OrderedDict(t[0:2] for t in license_type.LICENSE_TYPE)

CONCEPTS = {**EU_COUNTRIES,
            **FILE_TYPE,
            **FREQUENCY,
            **LICENSE_TYPE}

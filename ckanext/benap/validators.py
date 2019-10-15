# coding=utf-8
import re
from ckan.common import _

from ckan.logic.validators import Invalid

from ckanext.scheming.validation import scheming_validator

# pattern from http://phoneregex.com/
phone_number_pattern = re.compile(
    r"\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$"
)


def phone_number_validator(value, context):
    if value:
        if not phone_number_pattern.match(value):
            raise Invalid(_('Phone number {number} is not a valid format').format(number=value))
    return value


def countries_covered_belgium(value, context):
    if value:
        if len(value) != 0 and u'http://publications.europa.eu/resource/authority/country/BEL' not in value:
            raise Invalid(_('Belgium is a required country'))
    return value


def is_after_start(key, flattened_data, errors, context):
    temporal_end_dict = None
    try:
        for k in flattened_data:
            if k == ('__extras',):
                temporal_end_dict = flattened_data[k]
            elif k == (u'temporal_end',):
                if temporal_end_dict and temporal_end_dict.get('temporal_end_date', None) and \
                        temporal_end_dict.get('temporal_end_time', None):
                    flattened_data[k] = temporal_end_dict['temporal_end_date'] + ' ' + temporal_end_dict[
                        'temporal_end_time']
                elif temporal_end_dict and temporal_end_dict.get('temporal_end_date', None):
                    flattened_data[k] = temporal_end_dict['temporal_end_date'] + ' 00:00:00.000000'
                else:
                    flattened_data[k] = ''
    except KeyError:
        return True
    if temporal_end_dict:
        start_date = temporal_end_dict.get('temporal_start_date', '') + ' ' + \
                     temporal_end_dict.get('temporal_start_time', '')
        end_date = temporal_end_dict.get('temporal_end_date', '') + ' ' + temporal_end_dict.get('temporal_end_time', '')
        if temporal_end_dict.get('temporal_end_date', None):
            if start_date > end_date:
                raise Invalid(_('Start date must be before end date'))
    return True

# coding=utf-8
import re
import json
from itertools import count
from six import string_types
from ckan.common import _
from ckan.logic.validators import Invalid
from ckanext.scheming.validation import scheming_validator
import ckan.plugins.toolkit as toolkit
from ckan.lib.navl.dictization_functions import Missing
from ckanext.benap.helpers import (organisation_names_for_autocomplete, benap_get_organization_field_by_id,
                                   benap_get_organization_field_by_specified_field)

# pattern from http://phoneregex.com/
phone_number_pattern = re.compile(
    r"\+(9[976]\d|8[987530]\d|6[987]\d|5[90]\d|42\d|3[875]\d|2[98654321]\d|9[8543210]|8[6421]|6[6543210]|5[87654321]|4[987654310]|3[9643210]|2[70]|7|1)\d{1,14}$"
)

https_pattern = re.compile(
    r"^https:\/\/"
)

http_pattern = re.compile(
    r"^http:\/\/"
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


def remove_prefix(text, prefix):
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def https_validator(value, context):
    if value and value.startswith(('http', 'https')) and len(value) > 0:
        if not https_pattern.match(value):
            if http_pattern.match(value):
                value = remove_prefix(value, "http://")
            raise Invalid(_('URL {url} has to start with https://').format(url=value))
    return value


def modified_by_sysadmin(schema_value, package):
    # TODO: fix and re-enable this validator
    # Current implementation does not make sense, it is possible for
    # a non sysadmin user to set the value from true to false, this is not intended.
    return schema_value
    
    user = package.get("auth_user_obj")
    # parse schema_value
    trueValues = {"true"}
    flag = False

    if isinstance(schema_value, str):
        lowerValue = schema_value.strip().lower()
        if lowerValue in trueValues:
            flag = True

    if user is not None:
        if not user.sysadmin and flag:
            raise Invalid(_('Modification must done by a system administrator'))
        else:
            return schema_value
    else:
        raise Invalid(_('Logged in one must be'))


def is_choice_null(value):
    if isinstance(value, Missing) or value == '':
        return None
    return value


def contact_point_org_fields_consistency_check(key, flattened_data, errors, context):
    contact_point_name = flattened_data.get(('contact_point_name',))

    if contact_point_name in organisation_names_for_autocomplete():

        owner_org_id = flattened_data.get(('owner_org',))
        owner_org_title = benap_get_organization_field_by_id(owner_org_id, 'title')

        if owner_org_title == contact_point_name:
            owner_org = owner_org_id
        else:
            owner_org = benap_get_organization_field_by_specified_field(contact_point_name, 'id', 'title')

        if key == (u'contact_point_email',):
            contact_point_email = flattened_data.get(('contact_point_email',))
            publisher_email = benap_get_organization_field_by_id(owner_org, 'do_email')
            if contact_point_email != publisher_email:
                raise Invalid(
                    _('The contact point email must match the contact point organization\'s email: {}').format(
                        publisher_email))
        else:
            contact_point_tel = flattened_data.get(('contact_point_tel',))
            publisher_telephone_number = benap_get_organization_field_by_id(owner_org, 'do_tel')
            if contact_point_tel != publisher_telephone_number:
                raise Invalid(
                    _('The contact point telephone number must match the contact point organization\'s telephone number: {}').format(
                        publisher_telephone_number))


def fluent_tags_validator(key, flattened_data, errors, context):
    field_value = flattened_data.get(key)
    from ckantoolkit import h
    raw_choices = h.get_translated_tags()
    choices_list = [choice[0] for group in raw_choices for choice in group[0]]

    pattern = r"^[^,]+(,[^,]+)*$"
    if not field_value or not re.match(pattern, field_value):
        raise Invalid(_('Invalid format. Ensure the value is a comma-separated list of non-empty words.'))

    values = field_value.split(",")

    for value in values:
        if value not in choices_list:
            raise Invalid(_('Unexpected choice "%s".') % value)

def category_sub_category_validator(key, flattened_data, errors, context):
    # Retrieve the field value from the flattened data and parse it as a JSON object
    field_value = flattened_data.get(key)
    field_value = json.loads(field_value)

    # Extract the last element from the key to get the list item name
    list_item_name = key[-1]

    # Import the helper function to get the raw choices list
    from ckantoolkit import h
    raw_choices = h.benap_retrieve_raw_choices_list(list_item_name)

    # Build a choices dictionary where the key is the main category URL and the value is a list of associated
    # subcategory URLs
    choices_dict = {}
    for main_category, sub_categories in raw_choices:
        main_url = main_category[0][0]
        sub_urls = [sub_category[0] for sub_category in sub_categories]
        choices_dict[main_url] = sub_urls

    # Ensure that at least one main category is selected
    if not field_value:
        errors[key].append(_('Select at least one'))

    # Validate the main category and its subcategories in the field value
    for main_url, sub_urls in field_value.items():
        # Check if the main category exists in the result dictionary
        if main_url not in choices_dict:
            errors[key].append(_('unexpected choice "%s"') % main_url)
        else:
            # If there are subcategories, check if each one exists in the list of valid subcategories
            if sub_urls:
                for sub_url in sub_urls:
                    if sub_url not in choices_dict[main_url]:
                        errors[key].append(_('unexpected choice "%s"') % sub_url)

def license_fields_conditional_validation(key, flattened_data, errors, context):
    _, index, key_field_name = key
    def create_key(field_name):
        return ('resources', index, field_name)
    license_type = flattened_data.get(create_key('license_type'))
    conditions_usage = flattened_data.get(create_key('conditions_usage'))
    field_value = flattened_data.get(key)

    if conditions_usage == 'https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage/licence-provided':
        if key_field_name == 'license_type':
            if not field_value:
                raise Invalid(_('The license type is missing. This is required because "License" was chosen as the condition for usage.'))
        else:
            if license_type == 'Other':
                field_value = json.loads(field_value)
                if not field_value.get('en'):
                    raise Invalid(_('The license text is missing. At least the EN license text is required because'
                                    ' "Other" was chosen as the license type.'))

    else:
        if field_value:
            if key_field_name == 'license_type':
                raise Invalid(_('No license type should be given. "Contract" is chosen as the condition for usage.'))
            else:
                field_value = json.loads(field_value)
                if any(field_value.values()):
                    raise Invalid(_('No license text should be given. "Contract" is chosen as the condition for usage.'))


def benap_tag_string_convert(key, flattened_data, errors, context):
    '''
    Takes a list of tags that is a comma-separated string (in data[key])
    and parses tag names. These are added to the data dict, enumerated. They
    are also validated on the length.
    '''
    if isinstance(flattened_data[key], string_types):
        tags = [tag.strip() \
                for tag in flattened_data[key].split(',') \
                if tag.strip()]
    else:
        tags = flattened_data[key]

    tags = [url.split("/")[-1].capitalize() for url in tags]

    current_index = max( [int(k[1]) for k in flattened_data.keys() if len(k) == 3 and k[0] == 'tags'] + [-1] )

    for num, tag in zip(count(current_index+1), tags):
        flattened_data[('tags', num, 'name')] = tag

    for tag in tags:
        MIN_TAG_LENGTH = 1
        if len(tag) < MIN_TAG_LENGTH:
            raise Invalid(
                _('Tag "%s" length is less than minimum %s') % (tag, MIN_TAG_LENGTH)
            )
        MAX_TAG_LENGTH = 1000
        if len(tag) > MAX_TAG_LENGTH:
            raise Invalid(
                _('Tag "%s" length is more than maximum %i') % (tag, MAX_TAG_LENGTH)
            )

        tagname_match = re.compile('[\w \-.]*$', re.UNICODE)
        if not tagname_match.match(tag):
            raise Invalid(_('Tag "%s" must be alphanumeric '
                            'characters or symbols: -_.') % (value))

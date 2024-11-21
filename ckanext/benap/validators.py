# coding=utf-8
import re
import json
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
    user = package.get("auth_user_obj")
    # parse schema_value
    trueValues = {"true"}
    flag = False

    if isinstance(schema_value, str):
        lowerValue = schema_value.strip().lower()
        if lowerValue in trueValues:
            flag == True

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

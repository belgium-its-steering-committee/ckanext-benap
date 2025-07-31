# coding=utf-8
import json
import ckan.plugins.toolkit as toolkit
from ckan.common import config
import logging
from .decorators import decorator_timer
from itertools import chain

from ckanext.benap.helpers.lists import (NUTS1_BE, GEOREFERENCING_METHOD, DATASET_TYPE, NAP_TYPE, NETWORK_COVERAGE,
                                         MOBILITY_THEME, CONDITIONS_USAGE, CONDITIONS_ACCESS, LICENSE_TYPE, FREQUENCY,
                                         REFERENCE_SYSTEM, DATA_MODEL, SYNTAX, APPLICATION_LAYER_PROTOCOL, COMMUNICATION_METHOD, 
                                         GRAMMAR, ENCODING)
import ckanext.benap.constants.eu_authority as EU_AUTH_LISTS
from ckanext.benap.constants.nuts3_be import NUTS3_BE
from ckanext.benap.constants.mobilitydcat_ap.transport_mode import BY_CATEGORY as TRANSPORT_MODE_BY_CATEGORY

from ckanext.benap.util.forms import map_for_form_select
from ckanext.scheming.helpers import scheming_get_dataset_schema

log = logging.getLogger(__name__)

def user_language():
    try:
        from ckantoolkit import h
        return h.lang()
    except TypeError:
        return None  # lang() call will fail when no user language available


def ontology_helper(context):
    ontology = context.get("benap_helper_ontology", None)
    if ontology == "language":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/language/FRA', {
                "en": "French",
                "fr": "Français",
                "nl": "Frans",
                "de": "Französisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/ENG', {
                "en": "English",
                "fr": "Anglais",
                "nl": "Engels",
                "de": "Englisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/NLD', {
                "en": "Dutch",
                "fr": "Néerlandais",
                "nl": "Nederlands",
                "de": "Niederländisch"
            }),
            ('http://publications.europa.eu/resource/authority/language/DEU', {
                "en": "German",
                "fr": "Allemand",
                "nl": "Duits",
                "de": "Deutsch"
            }),
        ])

    elif ontology == "EU_COUNTRY":
        return map_for_form_select(EU_AUTH_LISTS.EU_COUNTRIES)
    elif ontology == "NUTS1_BE":
        return map_for_form_select(NUTS1_BE)
    elif ontology == "NUTS3_BE":
        return map_for_form_select(NUTS3_BE)
    elif ontology == "encoding":
        return map_for_form_select(ENCODING)

    elif ontology == "syntax":
        return map_for_form_select(SYNTAX)

    elif ontology == "grammar":
        return map_for_form_select(GRAMMAR)

    elif ontology == "datamodel":
        return map_for_form_select(DATA_MODEL)

    elif ontology == "protocol":
        return map_for_form_select(APPLICATION_LAYER_PROTOCOL)

    elif ontology == "communication":
        return map_for_form_select(COMMUNICATION_METHOD)

    elif ontology == "data-theme":
        return map_for_form_select([
            ('http://publications.europa.eu/resource/authority/data-theme/TRAN', {
                "en": "Transport",
                "fr": "Transports",
                "nl": "Vervoer",
                "de": "Verkehr"
            })
        ])
    elif ontology == "frequency":
        return map_for_form_select(FREQUENCY)
    elif ontology == "georeferencing_method":
        return map_for_form_select(GEOREFERENCING_METHOD)
    elif ontology == "dataset_type":
        return map_for_form_select(DATASET_TYPE)
    elif ontology == "nap_type":
        return map_for_form_select(NAP_TYPE)
    elif ontology == "network_coverage":
        return map_for_form_select(NETWORK_COVERAGE)
    elif ontology =="mobility_theme":
        values_labels_list = [item for sublist in get_translated_category_and_sub_category() for tuples in sublist for item in tuples]
        return map_for_form_select(values_labels_list)
    elif ontology == "conditions_access":
        return map_for_form_select(CONDITIONS_ACCESS)
    elif ontology == "conditions_usage":
        return map_for_form_select(CONDITIONS_USAGE)
    elif ontology == "license_type":
        return map_for_form_select(LICENSE_TYPE)
    elif ontology == "reference_system":
        return map_for_form_select(REFERENCE_SYSTEM)
    return None


# TODO: This translation should be done using the plugin translation mechanism
# It should be done in the IFacets implementation of this plugin
def translate_organization_filter(facet_title, lang):
    if facet_title == "Organizations":
        return {
            "en": "Organizations", 
            "nl": "Organisaties", 
            "fr": "Organisations", 
            "de": "Organisationen"}[lang]
    elif facet_title == "NAP Type":
        return {
            "en": "NAP type", 
            "nl": "NAP type", 
            "fr": "Type de NAP", 
            "de": "NAP typ"}[lang]
    return facet_title



def scheming_language_text_fallback(field_data, language_data):
    return field_data['en'] or field_data['nl'] or field_data['fr'] or field_data['de']


def package_notes_translated_fallback(package):
    notes_value = None
    user_lang = user_language()
    notes_translated = package.get('notes_translated', None)
    if notes_translated:
        if user_lang:
            notes_value = notes_translated.get(user_lang, None)
        if not notes_value:
            notes_value = notes_translated['en'] or notes_translated['nl'] or notes_translated['fr'] \
                          or notes_translated['de'] or None
    return notes_value


def field_translated_fallback(translated_field):
    field_value = None
    user_lang = user_language()
    if translated_field:
        if user_lang:
            field_value = translated_field.get(user_lang, None)
        if not field_value:
            field_value = translated_field['en'] or translated_field['nl'] or translated_field['fr'] \
                          or translated_field['de'] or None
    return field_value


def json_loads(data):
    return json.dumps(json.loads(data))


def forum_url():
    return config.get('ckan.pages.forum.link', '')


def organisation_names_for_autocomplete():
    from ckantoolkit import h
    return [org['title'] for org in h.organizations_available('create_dataset')]


def format_datetime(datetime):
    return datetime.replace('T', ' ')[:-7]


def scheming_language_text(field_data, language_data):
    return field_data[language_data]


def get_translated_tag_with_name(tagName, lang):
    return get_translated_tag(dict([(key, tagName) for key in {'name'}]), lang)


def get_translated_tag(tag, lang):
    tags = get_translated_tags()
    tags.append(tuple([NUTS1_BE]))
    tags.append(tuple([DATASET_TYPE]))
    tags.append(tuple([NAP_TYPE]))
    try:

        return [x for x in [translated_tag for translated_taglist in
                                                      [categorized_tags[0] for categorized_tags in
                                                       tags] for translated_tag in
                                                      translated_taglist] if x[0] == benap_tag_mapping(tag['name'])][0][1][lang]
    except:
        try:
            return tag['display_name']
        except KeyError:
            try:
                if isinstance(tag, str):
                    return tag
                print(('tag not found: ' + json.dumps(tag)))
            except:
                print('tag not found')


def get_translated_tags():
    return TRANSPORT_MODE_BY_CATEGORY


def get_translated_category_and_sub_category():
    return MOBILITY_THEME


def filter_default_tags_only(items):
    filtered_items = []
    tags = []
    for categorized_tags in get_translated_tags():
        for translated_tag in categorized_tags[0]:
            tags.append(translated_tag[0])
    for item in items:
        for tag in tags:
            if benap_tag_mapping(item['name']) == tag:
                filtered_items.append(item)
    return filtered_items


def is_default_tag(item):
    for categorized_tags in get_translated_tags():
        for translated_tag in categorized_tags[0]:
            if item['name'] == translated_tag[0]:
                return True
    show_element(item)
    return False


def getTranslatedVideoUrl(lang):
    switcher = {
        'en': 'https://www.youtube.com/embed/0-M48xzlWzI?rel=0&enablejsapi=1',
        'nl': 'https://www.youtube.com/embed/jle8RPRW1Do?rel=0&enablejsapi=1',
        'fr': 'https://www.youtube.com/embed/p8b9hIYM9hE?rel=0&enablejsapi=1',
        'de': 'https://www.youtube.com/embed/kB75uVs8oVo?rel=0&enablejsapi=1'
    }
    return switcher.get(lang, switcher.get('en'))


def get_organization_by_id(id):
    user = toolkit.get_action('get_site_user')(
        {
            'ignore_auth': True
        },
        {})

    context = {'user': user['name']}

    organization = toolkit.get_action('organization_show')(context,
    {
        'id': id,
        'include_dataset_count':False,
        'include_users': False,
        'include_groups': False,
        'include_tags': False,
        'include_followers': False,
    })
    field = 'display_title_' + user_language()
    to_show_name = organization.get(field)

    if (to_show_name):
        return to_show_name
    else:
        return organization.get('display_name')


def show_element(x):
    return x


def benap_fluent_label(field_name, field_label, lang):
    """
    Return a label for the input label for the given language
    """
    schema = scheming_get_dataset_schema('dataset')
    if schema:
        field_metadata = [x for x in schema['dataset_fields'] if x['field_name'] == field_name]
        if len(field_metadata) > 0:
            return field_metadata[0]['label'][lang]

    return field_label

def convert_validation_list_to_JSON(data):
    """
    Converts a string containing a JSON-like structure into a proper JSON list format.

    If the input string contains curly braces ('{', '}'), it is assumed to be a
    JSON-like structure and is converted by replacing the curly braces with square
    brackets ('[', ']'). If not, the string is wrapped in a JSON array format.

    This function is particularly useful for handling cases where a validation
    process converts a JSON string into a list format unexpectedly.
    """
    if '{' in data:
        data_string = data.replace('{', '[').replace('}', ']')
    else:
        data_string = '["{}"]'.format(data)
    return data_string

def benap_get_organization_field_by_id(org_id, field_name):
    """
    Retrieve the specified field value from an organization's data based on the organization id.
    """
    user = toolkit.get_action('get_site_user')(
        {
            'ignore_auth': True
        },
        {})
    context = {'user': user['name']}
    org_data = toolkit.get_action('organization_show')(context,
                                                        {
                                                            'id': org_id,
                                                            'include_dataset_count': False,
                                                            'include_users': False,
                                                            'include_groups': False,
                                                            'include_tags': False,
                                                            'include_followers': False,
                                                        })

    field_value = org_data.get(field_name)
    return field_value

def benap_get_organization_field_by_specified_field(org_value, field_name, search_field):
    """
    Retrieve the specified field value from an organization's data based on a specified search field.
    """
    from ckantoolkit import h
    org_list = h.organizations_available('create_dataset')

    org_data = next((org for org in org_list if org.get(search_field) == org_value), None)

    if org_data is None:
        return None

    field_value = org_data.get(field_name)
    return field_value

def benap_retrieve_dict_items_or_keys_or_values(data, return_type):
    """
    Retrieve keys, values, or both from a JSON-encoded dictionary.
    """
    if data:
        data = json.loads(data)

        if return_type == "keys":
            return list(data.keys())
        elif return_type == "values":
            return list(chain.from_iterable(list(data.values())))
        elif return_type == "items":
            return list(data.items())
    else:
        return []

def benap_retrieve_org_title_tel_email():
    """
    Retrieves a list of organizations where the current user can create datasets,
    including only the organization's title, telephone number, and email.
    """
    from ckantoolkit import h
    user = toolkit.get_action('get_site_user')(
        {
            'ignore_auth': True
        },
        {})
    context = {'user': user['name']}

    # organization_list has a limit of 25 orgs request at a time when all_fields is enabled
    # https://github.com/ckan/ckan/blob/2.11/ckan/logic/action/get.py#L346
    start = 0
    batch_size = 25
    all_orgs = []

    while True:
        batch = toolkit.get_action('organization_list')({}, {
            'include_dataset_count': False,
            'all_fields': True,
            'include_extras': True,
            'limit': batch_size,
            'offset': start
        })

        if not batch:
            break

        all_orgs.extend(batch)
        start += batch_size   
    keys_to_keep = ["title", "do_tel", "do_email"]
    filtered_props = [
        {key: item.get(key) for key in keys_to_keep}
        for item in all_orgs
    ]
    return filtered_props

def benap_retrieve_raw_choices_list(field_name):
    """
    Retrieve the raw choices list of a specified field
    """
    from ckanext.benap.helpers import lists
    return getattr(lists, field_name.upper())

def benap_tag_update_helper(data, choices):
    """
    Helper to remove old unused tags
    """
    if data:
        elements = data.split(',')
        valid_choices = [item[0] for sublist, _ in choices for item in sublist]
        filtered_elements = [element for element in elements if element in valid_choices]
        filtered_data = ','.join(filtered_elements)

        return filtered_data

    else:
        return None

def benap_tag_mapping(tag_name):
    """
    Create dictionary of tag mapping (tag name in table tag and url in table package_extra, fluent_tags)
    """
    urls = [item[0] for sublist, _ in get_translated_tags() for item in sublist]
    tag_mapping = {
        url.split("/")[-1].capitalize(): url
        for url in urls
    }
    return tag_mapping.get(tag_name)


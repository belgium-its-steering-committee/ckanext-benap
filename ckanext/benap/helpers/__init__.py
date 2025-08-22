# coding=utf-8
import json
import ckan.plugins.toolkit as toolkit
from ckan.common import config
import logging
from .decorators import decorator_timer
from itertools import chain
from ckan.logic import NotAuthorized
import re
from ckan.lib.helpers import get_site_protocol_and_host, lang, organizations_available

from ckanext.benap.helpers.lists import (NUTS1_BE, GEOREFERENCING_METHOD, DATASET_TYPE, NAP_TYPE, NETWORK_COVERAGE,
                                         CONDITIONS_USAGE, CONDITIONS_ACCESS, LICENSE_TYPE, FREQUENCY,
                                         REFERENCE_SYSTEM, DATA_MODEL, SYNTAX, APPLICATION_LAYER_PROTOCOL, COMMUNICATION_METHOD, 
                                         GRAMMAR, ENCODING)
from ckanext.benap.constants.mobility_theme_form import MOBILITY_THEME
from ckanext.benap.constants.concept_collections.eu_authority.country import EU_COUNTRIES
from ckanext.benap.constants.concept_collections.nuts import NUTS3_BE
from ckanext.benap.constants.mobilitydcat_ap.transport_mode import BY_CATEGORY as TRANSPORT_MODE_BY_CATEGORY
from ckanext.benap.constants.concept_collections.mobilitydcat import TRANSPORT_MODE as TRANSPORT_MODE_CONCEPTS

from ckanext.benap.util.forms import map_for_form_select
from ckanext.scheming.helpers import scheming_get_dataset_schema
from .concepts import get_concept_label

log = logging.getLogger(__name__)

def _c(concept_uri):
    """
A helper function striving to be the Python Babel equivalent of _(), but for skos concepts,
Taking the concept URI as an argument, and returning the localized label
    """
    return get_concept_label(concept_uri)

def get_facet_name_label_function(facet_name):
    facet_mapping = {
        'regions_covered_uri': _c,
        'mobility_theme_uri': _c,
        'format_uri': _c,
        'license_uri': _c,
        'tags': ckan_tag_to_transport_mode_concept_label,
    }
    if facet_name in facet_mapping:
        return facet_mapping[facet_name]

def get_facet_label_function(facet_name):
    fun = get_facet_name_label_function(facet_name)
    if fun:
        def fun_for_facet(_facet):
            return fun(_facet['name'])
        return fun_for_facet


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
        return map_for_form_select(EU_COUNTRIES)
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
        return lang_text({
            "en": "Organizations", 
            "nl": "Organisaties", 
            "fr": "Organisations", 
            "de": "Organisationen"}, lang)
    elif facet_title == "NAP Type":
        return lang_text({
            "en": "NAP type", 
            "nl": "NAP type", 
            "fr": "Type de NAP", 
            "de": "NAP typ"}, lang)
    return facet_title

def lang_text(translations, language = None, fallback = True):
    """
    return the translation (of current user locale by default) of a dict of translated strings in form:
    {
        "en": "English text",
        "nl": "Dutch text",
        "fr": "French text",
        "de": "German text"
    }
    If the chosen language is missing, it will fallback to other languages in order: en, nl, fr, de.
    This can be disabled by setting fallback to False.

    If no dict is passed, the function will return the result without any changes.
    This is a useful default for fields that can be both just a string or a dict of translations.
    """
    translation = translations[language or lang()] or None
    if not translation and fallback:
        # TODO: this order could come from ckan.locale_order config key
        translation = translations['en'] or translations['nl'] or translations['fr'] or translations['de'] or None
    return translation

# TODO: remove after replacing this with lang_text in fluent fork
def scheming_language_text_fallback(field_data, language_data):
    return lang_text(field_data)


def organisation_names_for_autocomplete():
    return [org['title'] for org in organizations_available('create_dataset')]


def format_datetime(datetime):
    return datetime.replace('T', ' ')[:-7]


# see lang_text for this with fallback (to all languages in order).
# Note that scheming_language_text helper comes from the scheming plugin (which fallbacks only to `en`),
# while this helper is refered to as benap_scheming_language_text (which does not fallback)
# TODO: this is a mess in the templates, both used in conjunction, and should be refactored.
# However note this is no trivial task: it is unclear for every usage if the fallback is desired or not.
def scheming_language_text(field_data, language_data):
    return field_data[language_data]


def get_translated_tags():
    return TRANSPORT_MODE_BY_CATEGORY


def get_translated_category_and_sub_category():
    return MOBILITY_THEME


def organization_name(organization):
    field = 'display_title_' + lang()
    to_show_name = organization.get(field)
    if (to_show_name):
        return to_show_name
    else:
        return organization.get('display_name')


def organization_by_id(id):
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
    return organization

def organization_name_by_id(id):
    return organization_name(organization_by_id(id))


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
    organization = organization_by_id(org_id)
    field_value = organization.get(field_name)
    return field_value

def benap_get_organization_field_by_specified_field(org_value, field_name, search_field):
    """
    Retrieve the specified field value from an organization's data based on a specified search field.
    """
    org_list = organizations_available('create_dataset')

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

def ckan_tag_to_transport_mode_concept_uri(tag_name):
    """
    Return the transport mode skos:Concept uri for the supplied CKAN dataset "tag" name.
    The tag names correspond to the (capitalized) last portion of the concept uri
    """
    urls = TRANSPORT_MODE_CONCEPTS.keys()
    tag_mapping = {
        url.split("/")[-1].capitalize(): url
        for url in urls
    }
    return tag_mapping.get(tag_name)

def parse_embedded_links(string_with_links):
    """
    Parse string text that contains links. Links should be added as `<a href="/your/link">link text</a>`.
    If the link start with `/`, it is considered as a relative link
    and will automatically get prefixed with the correct language code. (e.g. `/pages/your-page` becomes `/en/pages/your-page`)
    if not, the link is kept as is.
    :param string_with_links: input string containing <a href="...">link text</a>
    :return: list of parts with text and href information. If no links, will contain one (normal-text) part
    """
    parts_list = []

    # match <a href='...'>link text</a>
    pattern = r'<a\s+href=["\']([^"\']+)["\'][^>]*>([^<]+)</a>'

    last_link_match_end = 0
    for match in re.finditer(pattern, string_with_links):
        # text starting from end last link (or beginning) till before this link
        parts_list.append({
            "text": string_with_links[last_link_match_end:match.start()],
            "href": None
        })

        # link itself
        href = match.group(1)
        link_text = match.group(2)

        if href.startswith('/'):
            protocol, host = get_site_protocol_and_host()
            if protocol and host:
                href = f"{protocol}://{host}/{lang()}{href}"

        parts_list.append({ "text": link_text,"href": href })

        last_link_match_end = match.end()

    # text after last link
    if last_link_match_end < len(string_with_links):
        parts_list.append({ "text": string_with_links[last_link_match_end:], "href": None })

    return parts_list


def is_member_of_org(org_id, user_id):
    if not user_id:
        return False
    try:
        members = toolkit.get_action('member_list')({}, {
            'id': org_id
        })

        return any(
            member_type == 'user' and member_id == user_id
            for member_id, member_type, _ in members
        )
    except NotAuthorized:
        return False


def ckan_tag_to_transport_mode_concept_label(tag_name):
    transport_mode_concept_uri = ckan_tag_to_transport_mode_concept_uri(tag_name)
    transport_mode_label = _c(transport_mode_concept_uri)
    return transport_mode_label

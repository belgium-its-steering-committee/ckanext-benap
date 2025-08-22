#!/usr/bin/env python3

import logging

from ckanext.benap.constants.concept_collections import CONCEPTS
from ckan.lib.helpers import lang

log = logging.getLogger(__name__)

def get_concept_label(concept_uri, language = None, collection=CONCEPTS):
    try:
        concept = collection[concept_uri]
        if isinstance(concept, dict):
            try:
                return concept[language or lang()]
            except KeyError as e:
                log.error(f"No language {language or lang()} known for concept \"{concept_uri}\"")
                raise e
        else:
            # The same string value for all languages
            return concept
    except KeyError as e:
        # TODO: some skos concept-scheme (URI!) based forms contain strings like "Other" or "XML" as an option.
        # this should probably be refactored out. For now, just return that string value instead.
        log.error(f"No concept known by uri \"{concept_uri}\"")
        return concept_uri

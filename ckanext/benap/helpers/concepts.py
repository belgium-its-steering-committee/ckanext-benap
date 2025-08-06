#!/usr/bin/env python3

import logging

from ckanext.benap.constants.concept_collections import CONCEPTS

log = logging.getLogger(__name__)

def get_concept_label(concept_uri, lang, collection=CONCEPTS):
    try:
        concept = collection[concept_uri]
        if isinstance(concept, dict):
            try:
                return concept[lang]
            except KeyError:
                log.error(f"No language {lang} known for concept \"{concept_uri}\"")
        else:
            # The same string value for all languages
            return concept
    except KeyError:
        log.error(f"No concept known by uri \"{concept_uri}\"")

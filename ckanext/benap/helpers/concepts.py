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
            except KeyError as e:
                log.error(f"No language {lang} known for concept \"{concept_uri}\"")
                raise e
        else:
            # The same string value for all languages
            return concept
    except KeyError as e:
        # TODO: some skos concept-scheme (URI!) based forms contain the string "Other" as an option.
        # This should probably be refactored out.
        if concept_uri == "Other":
            return "Other"
        log.error(f"No concept known by uri \"{concept_uri}\"")
        raise e

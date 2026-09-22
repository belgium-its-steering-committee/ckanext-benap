import json
from ckanext.dcat.harvesters.rdf import DCATRDFHarvester
from ckanext.dcat.profiles.base import RDFProfile
import ckan.plugins.toolkit as toolkit
from ckan.plugins.core import SingletonPlugin, implements
from ckanext.harvest.interfaces import IHarvester

EMPTY_VALUES = (None, [], (), "", {})

class _BenapDCATRDFHarvester(DCATRDFHarvester):
    def validate_config(self, source_config):
        source_config = super().validate_config(source_config)
        if not source_config:
            return source_config

        source_config_obj = json.loads(source_config)

        if not isinstance(source_config_obj.get("package_defaults", {}), dict):
            raise ValueError("package_defaults must be a dictionary")
        if not isinstance(source_config_obj.get("package_overrides", {}), dict):
            raise ValueError("package_overrides must be a dictionary")

    def modify_package_dict(self, package_dict, dcat_dict, harvest_object):
        config = json.loads(harvest_object.source.config)
        package_defaults = config.get("package_defaults", {})
        package_overrides = config.get("package_overrides", {})
        resource_defaults = config.get("resource_defaults", {})
        resource_overrides = config.get("resource_overrides", {})

        existing_dataset = self._get_existing_dataset(harvest_object.guid) or {}

        # Create an empty parser to have access to utility functions
        _parser = RDFProfile(None)

        for key, value in package_defaults.items():
            if self._get_dict_value(package_dict, key) in (None, [], (), "", {}):
                if key == "private":
                    package_dict["private"] = existing_dataset.get(key, value)
                else:
                    _parser._set_dataset_value(
                        package_dict, key, existing_dataset.get(key, value)
                    )

        for key, value in package_overrides.items():
            _parser._set_dataset_value(package_dict, key, value)

        for resource_dict in package_dict["resources"]:
            for key, value in resource_defaults.items():
                if resource_dict.get(key) in EMPTY_VALUES:
                    resource_dict[key] = value
            for key, value in resource_overrides.items():
                resource_dict[key] = value

        return package_dict


class BenapDCATRDFHarvester(SingletonPlugin):
    """
    RDF Harvester with attribute defaults and overrides

    Example config::
      {
        "rdf_format": "application/rdf+xml",
        "user": "default",
        "package_defaults": {
          "private": true,
          "cont_res": "",
          "nap_type": [],
          "agreement_declaration_nap": ["Y"],
          "countries_covered": [
            "http://publications.europa.eu/resource/authority/country/BEL"
          ],
          "regions_covered": ["http://data.europa.eu/nuts/code/BE2"],
          "theme": "http://publications.europa.eu/resource/authority/data-theme/TRAN"
        },
        "resource_defaults": {
          "conditions_access": "",
          "conditions_usage": ""
        },
        "resource_overrides": {
          "format": "http://publications.europa.eu/resource/authority/file-type/XML"
        }
      }

    """

    implements(IHarvester, inherit=False)

    # We use this proxy trick because if we inherit directly from
    # DCATRDFHarvester, then only the parent class will be registered.
    def __init__(self, *args, **kwargs):
        self._harvester = _BenapDCATRDFHarvester(*args, **kwargs)

    def __getattr__(self, attr):
        return getattr(self._harvester, attr)

    def info(self):
        return {
            "name": "benap_dcat_rdf",
            "title": "Benap DCAT RDF Harvester",
            "description": "Harvester for DCAT datasets from an RDF graph, customized for beNAP",
        }

import json
from ckanext.dcat_be_napits.profiles.euro_mobility_dcat_ap import EuropeanMobilityDCATAPProfile
from ckanext.benap.constants.mobility_theme_form import MOBILITY_THEME_BROADER_NARROWER_MAPPING

BROAD_THEMES = set(broader for (broader, _narrower) in MOBILITY_THEME_BROADER_NARROWER_MAPPING)
NARROW_THEMES = dict(
    (narrower, broader)
    for (broader, narrowers) in MOBILITY_THEME_BROADER_NARROWER_MAPPING
    if narrowers
    for (narrower, _names) in narrowers
)

RIGHTS_MAPPING = dict(
    (
        f"https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage/{key}",
        (
            f"https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage/{access}" if access else None,
            f"https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage/{usage}" if usage else None,
        ),
    )
    for key, (access, usage) in [
        ("contractual-arrangement", (None, "contractual-arrangement")),
        ("contractual-arrangement-fee-required", ("fee-required", "contractual-arrangement")),
        ("contractual-arrangement-free-of-charge", ("free-of-charge", "contractual-arrangement")),
        ("fee-required", ("fee-required", None)),
        ("free-of-charge", ("free-of-charge", None)),
        ("licence-provided", (None, "licence-provided")),
        ("licence-provided-fee-required", ("fee-required", "licence-provided")),
        ("licence-provided-free-of-charge", ("free-of-charge", "licence-provided")),
        ("other", (None, None)),
        ("royalty-free", ("free-of-charge", "licence-provided")),
    ]
)

CONDITIONS_USAGE_LICENSE = "IRI: https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage/licence-provided"

class BenapProfile(EuropeanMobilityDCATAPProfile):

    def parse_dataset(self, dataset_dict, dataset_ref):
        dataset_dict = super().parse_dataset(dataset_dict, dataset_ref)

        # Date fields
        temporal_start = self._get_dict_value(dataset_dict, 'temporal_start')
        if temporal_start:
            self._set_dataset_value(dataset_dict, 'temporal_start_date',  temporal_start + '')
        temporal_end = self._get_dict_value(dataset_dict, 'temporal_end')
        if temporal_end:
            self._set_dataset_value(dataset_dict, 'temporal_end_date',  temporal_end + '')

        # Mobility theme
        flat_mobility_themes = (self._get_dict_value(dataset_dict, 'mobility_theme'))
        dict_mobility_themes = dict()

        for theme in flat_mobility_themes:
            broader, narrower = self._mobility_theme_lookup(theme)
            narrowers = dict_mobility_themes.setdefault(broader, list())
            if narrower:
                narrowers.append(narrower)

        self._set_dataset_value(dataset_dict, 'mobility_theme', dict_mobility_themes)

        # Renamed fields
        rename_fields = {
            'contact_name': 'contact_point_name',
            'contact_email': 'contact_point_email',
            'contact_tel': 'contact_point_tel',
        }

        for old, new in rename_fields.items():
            self._set_dataset_value(
                dataset_dict, new, self._get_dict_value(dataset_dict, old)
            )

        # Resources
        for distribution in self._distributions(dataset_ref):
            distribution_ref = str(distribution)
            for resource_dict in dataset_dict.get("resources", []):
                # Match distribution in graph and distribution in resource dict
                if resource_dict and distribution_ref == resource_dict.get(
                    "distribution_ref"
                ):

                    rights_types = self._get_resource_value(resource_dict, 'rights_types')
                    for right in rights_types:
                        access, usage = self._access_usage_lookup(right)

                        if access:
                            resource_dict["conditions_access"] = access
                        if usage:
                            resource_dict["conditions_usage"] = usage

                    if resource_dict["conditions_usage"] != CONDITIONS_USAGE_LICENSE:
                        del resource_dict["license_type"]
                        del resource_dict["license_text_translated"]

        dataset_dict['spatial'] = self._get_dataset_value(dataset_dict, 'spatial')
        dataset_dict['temporal_start_date'] = self._get_dataset_value(dataset_dict, 'temporal_start_date')
        dataset_dict['temporal_start_time'] = '00:00:00'
        dataset_dict['temporal_start_tz'] = 'UTC'
        dataset_dict['temporal_end_date'] = self._get_dataset_value(dataset_dict, 'temporal_end_date')
        dataset_dict['temporal_end_time'] = '00:00:00'
        dataset_dict['temporal_end_tz'] = 'UTC'

        dataset_dict['extras'] = [
            entry
            for entry in dataset_dict['extras']
            if entry['key'] not in map((lambda f: f['field_name']), self._dataset_schema['dataset_fields'])
        ]

        return dataset_dict

    def _mobility_theme_lookup(self, mobility_theme) -> tuple[str, str | None]:
        if mobility_theme in NARROW_THEMES:
            return (NARROW_THEMES[mobility_theme], mobility_theme)
        elif mobility_theme in BROAD_THEMES:
            return (mobility_theme, None)
        else:
            raise ValueError(f"Unknown mobility theme: '{mobility_theme}'")

    def _access_usage_lookup(self, right) -> tuple[str | None, str | None]:
        access_usage = RIGHTS_MAPPING.get(right)
        if access_usage:
            return access_usage
        else:
            raise ValueError(f"Unknown right type: {right}")

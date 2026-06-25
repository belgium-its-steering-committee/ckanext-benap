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

    def _mobility_theme_lookup(self, mobility_theme):
        if mobility_theme in NARROW_THEMES:
            return (NARROW_THEMES[mobility_theme], mobility_theme)
        elif mobility_theme in BROAD_THEMES:
            return (mobility_theme, None)
        else:
            raise ValueError(f"Unknown mobility theme: '{mobility_theme}'")

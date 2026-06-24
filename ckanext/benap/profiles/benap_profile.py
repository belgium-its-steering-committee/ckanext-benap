from ckanext.dcat_be_napits.profiles.euro_mobility_dcat_ap import EuropeanMobilityDCATAPProfile

class BenapProfile(EuropeanMobilityDCATAPProfile):

    def parse_dataset(self, dataset_dict, dataset_ref):
        dataset_dict = super().parse_dataset(dataset_dict, dataset_ref)


        # Date fields
        if temporal_start := self._get_dict_value(dataset_dict, 'temporal_start'):
            dataset_dict['temporal_start'] = temporal_start + 'T00:00:00Z'
        if temporal_end := self._get_dict_value(dataset_dict, 'temporal_end'):
            dataset_dict['temporal_end'] = temporal_end + 'T00:00:00Z'

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

        return dataset_dict

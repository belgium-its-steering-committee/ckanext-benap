
def map_for_form_select(tuple_list):
    """

    :param tuple_list: array of tuples (key, value)
    :return: json array suitable for CKAN's form.select
    """
    return [{'value': t[0], 'label': t[1]} for t in tuple_list]

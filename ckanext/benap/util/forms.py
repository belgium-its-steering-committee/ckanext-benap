
def map_for_form_select(tuple_list, x):
    """

    :param tuple_list: array of tuples (key, value)
    :return: json array suitable for CKAN's form.select
    """
    print("#"*35)
    print(x)
    print("#"*35)
    return [{'value': t[0], 'label': t[1]} for t in tuple_list]

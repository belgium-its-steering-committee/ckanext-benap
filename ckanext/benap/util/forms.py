def map_for_form_select(tuple_list):
    """
    :param tuple_list: array of tuples (key, value)
    :return: json array suitable for CKAN's form.select
    """
    return [{'value': t[0], 'label': t[1]} for t in tuple_list]
  
def soft_compare_strings(value1, value2):
    """
    Compares two values, but handle booleans.
    Can be extended to handle more "types".
    """
    is_boolean_str = str(value1).lower() in ['true', 'false'] and str(value2).lower() in ['true', 'false']
    if is_boolean_str:
        return str(value1).lower() == str(value2).lower()
    return value1 == value2
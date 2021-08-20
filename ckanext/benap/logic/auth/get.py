from ckanext.benap.helpers import show_element


def user_list(context, data_dict=None):
    """Check whether access to the user list is authorised. Restricted to admins only."""
    return {'success': False}


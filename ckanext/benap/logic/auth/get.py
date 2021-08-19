from ckanext.benap.helpers import show_element


def user_list(context, data_dict=None):
    """Check whether access to the user list is authorised. Restricted to admins only."""
    return {'success': False}


def organization_show(context, data_dict=None):
    """Allow everyone to access organization data (for translated organization data helper)"""
    return {'success': True}


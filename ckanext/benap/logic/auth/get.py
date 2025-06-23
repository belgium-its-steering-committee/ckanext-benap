def user_list(context, data_dict=None):
    """Check whether access to the user list is authorised. Restricted to sys-admins only."""
    # Uncertain why this is blocked and if it can be unblocked, so a specific auth function is created for user_autocomplete
    return {'success': False}

def user_autocomplete(context, data_dict=None):
    """Allow autocompleting users so users can be searched when adding to an organization"""
    return {'success': True}

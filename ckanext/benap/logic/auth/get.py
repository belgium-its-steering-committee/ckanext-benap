
def user_list(context, data_dict):
    """Check whether access to the user list is authorised. Restricted to admins only."""
    return dict(success=False)
    # return {'success': False}

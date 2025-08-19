import ckan.plugins.toolkit as tk
import ckan.authz as authz

def user_list(context, data_dict=None):
    """Check whether access to the user list is authorised. Restricted to sys-admins only."""
    # Uncertain why this is blocked and if it can be unblocked, so a specific auth function is created for user_autocomplete
    return {'success': False}

def user_autocomplete(context, data_dict=None):
    """Allow autocompleting users so users can be searched when adding to an organization"""
    return {'success': True}

def member_list(context, data_dict):
    user = context.get('user')
    model = context['model']
    session = model.Session

    org_id = data_dict.get('id')

    if not org_id:
        return {'success': False, 'msg': 'Organization ID not provided'}

    user_obj = tk.get_action('user_show')({'ignore_auth': True}, {'id': user})
    if not user_obj:
        return {'success': False, 'msg': 'User not found'}

    # Check if the user is a member of the org
    if authz.has_user_permission_for_group_or_org(
        org_id, user, 'read'
    ):
        return {'success': True}
    
    return {'success': False, 'msg': 'User is not a member of the organization'}
import ckan.plugins.toolkit as tk
from ckan.logic.action.get import organization_show as vanilla_organization_show
from ckan.lib.helpers import url_for_static

# Copied from https://github.com/belgium-its-steering-committee/ckanext-scheming/blob/MobilityDCAT/root/ckanext/scheming/logic.py#L85
@tk.side_effect_free
def organization_show(context, data_dict):
    """
    adjust contents of image_display_url
    """

    result_dict = vanilla_organization_show(context, data_dict)

    #API restriction for not logged-in users

    user_name = context['user']

    def user_is_member_of_org():
        if not user_name:
            return False

        organization_id = result_dict.get('id', None)
        user_org_dict = tk.get_action('organization_list_for_user')(
            data_dict={'id': user_name})

        return any(org['id'] == organization_id for org in user_org_dict) 

    if not user_name or (not user_is_member_of_org() and user_name != 'napcontrolbody'):
        #extra pops on NAP request
        popList = ['rtti_doc_document_upload',
                   'srti_doc_document_upload',
                   'sstp_doc_document_upload',
                   'optional_comment',
                   'agreement_declaration_mmtis',
                   'organization_agreement_declaration_nap',
                   'proxy_pdf_url']
        
        for item in popList:
            if item in result_dict:
                result_dict.pop(item)

    #END API restriction   
    

    image_url = result_dict.get('image_url', '')
    organization_name = result_dict.get('name', None)
    if organization_name and not image_url.startswith(('http', 'https')) and len(image_url) > 0:
        result_dict['image_display_url'] = url_for_static(
            'uploads/organization/{0}/{1}'.format(organization_name, result_dict.get('image_url')),
            qualified=True
        )
        
    return result_dict
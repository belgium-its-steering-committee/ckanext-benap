import ckan.plugins.toolkit as tk
from ckan.logic.action.get import organization_show as vanilla_organization_show
from ckan.lib.helpers import url_for_static
from ckan import model
import sqlalchemy
from ckanext.benap.constants import DOC_FIELDS

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

# Also search in display_title_* fields (translations of title)
@tk.chained_action
def organization_list(original_action, context, data_dict):
    q_original = data_dict.get('q', '').strip()
    if not q_original:
        return original_action(context, data_dict)

    model = context['model']
    group_type = data_dict.get('type', 'organization')
    q = u'%{0}%'.format(q_original)

    # The description is a {en: .., fr: ..} field, but for search this can just be seen as plain text.
    # however, will return everything if q equal to 'fr', 'nl', 'de' or 'en', so don't include
    # it in those cases.
    extra_keys = ['display_title_en', 'display_title_fr', 
                   'display_title_nl', 'display_title_de']
    if q_original not in ['en', 'fr', 'nl', 'de']:
        extra_keys.append('description_translated')

    query = model.Session.query(model.Group.name) \
      .filter(model.Group.state == 'active') \
      .filter(model.Group.is_organization == True) \
      .filter(model.Group.type == group_type)

    query = query.outerjoin(model.GroupExtra, 
                            model.GroupExtra.group_id == model.Group.id)  
    query = query.filter(sqlalchemy.or_(
                        model.Group.name.ilike(q),
                        model.Group.title.ilike(q),
                        model.Group.description.ilike(q),
                        sqlalchemy.and_(model.GroupExtra.key.in_(extra_keys), model.GroupExtra.value.ilike(q)),
                    )) \
                 .distinct()

    matched_names = [name for (name,) in query.all()]

    # Use the organizations property of organization_list to only search/filter on that list of orgs
    # This way we can keep the original sorting,pagination,access control...
    # but return these specified orgs. Remove the query param to avoid further filtering.
    if matched_names:
      del data_dict['q']
      data_dict['organizations'] = matched_names
    return original_action(context, data_dict)

@tk.chained_action
def organization_create(original_action, context, data_dict):
    return _organization_change(original_action, context, data_dict)
@tk.chained_action
def organization_update(original_action, context, data_dict):
    return _organization_change(original_action, context, data_dict)
@tk.chained_action
def organization_patch(original_action, context, data_dict):
    return _organization_change(original_action, context, data_dict)

def _organization_change(original_action, context, data_dict):
    organization = original_action(context, data_dict)

    files = [data_dict[doc] for doc in DOC_FIELDS.keys() if data_dict[doc]]
    if files:
        # TODO: move this to a background job
        sysadmins = \
            model.Session.query(model.User) \
            .filter(model.User.sysadmin) \
            .all()

        for sysadmin in sysadmins:
            if not sysadmin.email:
                continue
            for file in files:
                compliance_type = DOC_FIELDS[file.name]
                render_vars = {
                    'user_name': sysadmin.display_name or sysadmin.name,
                    'organization_title': data_dict['title'],
                    'organization_url': tk.url_for('organization.about', _external=True, id=data_dict['id']),
                    'compliance_type': compliance_type
                }
                # TODO: i18n (for the sysadmin, not for the uploader)
                subject = tk.render('emails/doc_notify_subject.txt', render_vars)
                body = tk.render('emails/doc_notify.txt', render_vars)
                body_html = tk.render('emails/doc_notify.html', render_vars)

                tk.mail_user(
                    recipient=sysadmin,
                    subject=subject,
                    body=body,
                    body_html=body_html
                )

    return organization

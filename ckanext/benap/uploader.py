# Copied from https://github.com/belgium-its-steering-committee/ckanext-scheming/blob/MobilityDCAT/root/ckanext/scheming/lib/uploader.py#L2
# encoding: utf-8
import cgi
import logging
import mimetypes
import magic
import os
import datetime
import ckan.lib.munge as munge
from ckan.plugins import toolkit as tk

from ckan.lib.uploader import get_storage_path, get_max_image_size, get_max_resource_size
from werkzeug.datastructures import FileStorage as FlaskFileStorage

from ckanext.benap.helpers import benap_get_organization_field_by_id

from ckanext.clamav.utils import scan_file_for_viruses as clamav_scan_file_for_viruses


ALLOWED_UPLOAD_TYPES = (cgi.FieldStorage, FlaskFileStorage)
MB = 1 << 20

log = logging.getLogger(__name__)

_storage_path = None
_max_resource_size = None
_max_image_size = None

def scan_file_for_viruses(field_name, file):
    # plugin needs a "data_dict" with FileStorage in "upload"
    # It also expects an "id" for use in logging, but is hardcoded to only work for resources.
    # We don't pass an "id", meaning it might give some wrong logging messages that the package is not created yet.
    # TODO: reimplement this function for this organization usecase.
    try:
        return clamav_scan_file_for_viruses({"upload": file})
    except tk.ValidationError as e:
        raise tk.ValidationError({field_name: [e.message]})

def organization_storage_dir(org_id):
    path = get_storage_path()
    if not path:
        return None
    return os.path.join(path, 'storage', 'uploads', 'organization', org_id)


def get_max_pdf_size() -> int:
    return tk.config.get('ckan.max_pdf_size')

def _copy_file(field_name ,input_file, output_file, max_size):
    input_file.seek(0)
    current_size = 0
    while True:
        current_size = current_size + 1
        # MB chunks
        data = input_file.read(MB)

        if not data:
            break
        output_file.write(data)
        if current_size > max_size:
            raise tk.ValidationError({field_name: ['File upload too large']})


def _get_underlying_file(wrapper):
    if isinstance(wrapper, FlaskFileStorage):
        return wrapper.stream
    return wrapper.file


def _make_dirs_if_not_existing(storage_path):
    if os.path.isdir(storage_path):
        pass
    else:
        try:
            os.makedirs(storage_path)
        except OSError as e:
            # errno 17 is file already exists
            if e.errno != 17:
                raise


class OrganizationUploader(object):
    def __init__(self, upload_fields):
        """ Setup upload by creating a subdirectory of the storage directory
        for organization uploads. Handle multiple upload fields passed in upload_fields.
        upload_fields is a list of dictionaries with the following keys:
          field_name: where filename is stored
          file_field: upload field name
          clear_field: clear checkbox field name
          file_type: file type to verify (image or pdf)
          old_file_field_name: Optional (same as field_name by default). Name to retrieve old filename from organization
          max_size: Optional, default taken via env variables. Used to override this default value.
        """
        self.storage_path = None
        path = get_storage_path()
        if not path:
            return
        self.storage_path = os.path.join(path, 'storage', 'uploads', 'organization')
        _make_dirs_if_not_existing(self.storage_path)

        self.file_uploaders = []
        for field_config in upload_fields:
            # backwards compatibility with how this code worked before: only proxy_pdf_url used non-legacy munge_filename
            if field_config['field_name'] == 'proxy_pdf_url':
                field_config['use_munge_filename_legacy'] = False
            
            self.file_uploaders.append(FileUploader(field_config, self.storage_path))

    def update_data_dict(self, data_dict, _url_field, _file_field, _clear_field):
        """ Manipulate data from the data_dict. Ignore input parameters: these are focussed on logo upload only.
        This is called before it reaches any validators.
        """
        if not self.storage_path:
            return

        for file_uploader in self.file_uploaders:
            file_uploader.update_data_dict(data_dict)

    def upload(self, _max_size=None):
        """ Actually upload the file.
        This happens just before a commit but after the data has
        been validated and flushed to the db. This is so we do not store
        anything unless the request is actually good.
        """
        for file_uploader in self.file_uploaders:
            file_uploader.upload()


class FileUploader(object):
    def __init__(self, field_config, storage_path):
        """Initialize a FileUploader for a single upload field.
        
        Args:
            field_config: Dictionary with keys: field_name, file_field, clear_field,
                         file_type, old_file_field_name (optional), max_size (optional)
            storage_path: Base storage path for uploads
        """
        self.field_name = field_config['field_name']
        self.file_field = field_config['file_field']
        self.clear_field = field_config['clear_field']
        self.file_type = field_config['file_type']
        self.old_file_field_name = field_config.get('old_file_field_name', self.field_name)
        # Default use legacy for backwards compatibility when PATCHing organizations
        # to ensure filenames don't appear changed when they haven't.
        # For new file types, use_munge_filename_legacy can be set to False.
        # TODO: Check if existing filenames can be migrated and legacy munging can be removed.
        self.use_munge_filename_legacy = field_config.get('use_munge_filename_legacy', True)
        self.storage_path = storage_path
        self.max_size = field_config.get('max_size', None)
        if self.max_size is None:
            if self.file_type == 'image':
                self.max_size = get_max_image_size()
            elif self.file_type == 'pdf':
                self.max_size = get_max_pdf_size()
            else:
                raise ValueError(f"Unsupported file_type: {self.file_type}")

        self.clear = None
        self.upload_field_storage = None
        self.filename = None
        self.filepath = None
        self.tmp_filepath = None
        self.upload_file = None
        self.old_filename = None
        self.old_filepath = None

    def update_data_dict(self, data_dict):
        """Manipulate data from the data_dict for this upload field.
        This needs to be called before it reaches any validators.
        """
        if not self.storage_path:
            return

        # get old filename from existing organization
        try:
            self.old_filename = benap_get_organization_field_by_id(
                data_dict.get('name'), self.old_file_field_name)
        except tk.ObjectNotFound:
            self.old_filename = None

        if self.old_filename:
            self.old_filepath = os.path.join(
                self.storage_path, data_dict.get('name'), self.old_filename)

        self.clear = data_dict.get(self.clear_field, None)
        self.upload_field_storage = data_dict.get(self.file_field, None)

        if isinstance(self.upload_field_storage, ALLOWED_UPLOAD_TYPES):
            if self.upload_field_storage.filename:
                self.filename = self.upload_field_storage.filename
                self.filename = str(datetime.datetime.utcnow()) + self.filename
                if self.use_munge_filename_legacy:
                    self.filename = munge.munge_filename_legacy(self.filename)
                else:
                    self.filename = munge.munge_filename(self.filename)

                # this is still coupled with organization upload.
                # If FileUploader needs to be used more broadly, refactor this.
                organization_storagepath = os.path.join(self.storage_path, data_dict.get('name'))
                _make_dirs_if_not_existing(organization_storagepath)
                self.filepath = os.path.join(organization_storagepath, self.filename)
                data_dict[self.field_name] = self.filename
                data_dict['url_type'] = 'upload'
                self.upload_file = _get_underlying_file(self.upload_field_storage)
                self.tmp_filepath = self.filepath + '~'
                self._verify_type()
                
                scan_file_for_viruses(self.field_name, self.upload_field_storage)

        # Keep the file if there has been no change
        elif self.old_filename and not self.old_filename.startswith('http'):
            if not self.clear:
                data_dict[self.field_name] = self.old_filename
            elif self.clear:
                data_dict[self.field_name] = ''

    def upload(self, _max_size=None):
        """Actually upload the file.
        This should happen just before a commit but after the data has
        been validated and flushed to the db. This is so we do not store
        anything unless the request is actually good."""
        if self.filename:
            assert self.upload_file and self.filepath
            with open(self.tmp_filepath, 'wb+') as output_file:
                try:
                    _copy_file(self.field_name, self.upload_file, output_file, self.max_size)
                except tk.ValidationError:
                    os.remove(self.tmp_filepath)
                    raise
                finally:
                    self.upload_file.close()
            os.rename(self.tmp_filepath, self.filepath)
            self.clear = True

        if (self.clear and self.old_filename
                and not self.old_filename.startswith('http')
                and self.old_filepath):
            try:
                os.remove(self.old_filepath)
            except OSError:
                pass

    def _verify_type(self):
        """Verify the file type matches the expected type for this upload field.
        Adjustment from verify_type in ckan-core/ckan/lib/uploader.py to allow
        specifying more specific mimetypes per upload field.
        """
        
        def raise_upload_type_error(bad_type):
            raise tk.ValidationError(
                { self.file_field: [ f"Type error - Unsupported upload type: {bad_type}" ] }
            )
        
        if not self.upload_file:
            return
        # allowed_types is the first "part" of the mimetype
        if self.file_type == "image":
            allowed_mimetypes = ["image/jpg", "image/jpeg", "image/png", "image/bmp"]
            allowed_types = ["image"]
            allowed_extensions = ['.jpeg', '.jpg', '.bmp', '.png']
        elif self.file_type == "pdf":
            allowed_mimetypes = ["application/pdf"]
            allowed_types = ["application"]
            allowed_extensions = ['.pdf']
        else:
            return  

        # Check that the declared types in the request are supported
        declared_mimetype_from_filename = mimetypes.guess_type(
            self.upload_field_storage.filename
        )[0]
        declared_content_type = self.upload_field_storage.content_type
        for declared_mimetype in (
            declared_mimetype_from_filename,
            declared_content_type,
        ):
            if (declared_mimetype and declared_mimetype not in allowed_mimetypes):
                  raise_upload_type_error(declared_mimetype)

        # Check that the actual type guessed from the contents is supported
        content = self.upload_file.read(2048)
        guessed_mimetype = magic.from_buffer(content, mime=True)

        self.upload_file.seek(0, os.SEEK_SET)

        if guessed_mimetype not in allowed_mimetypes:
            raise_upload_type_error(guessed_mimetype)

        type_ = guessed_mimetype.split("/")[0]
        if type_ not in allowed_types:
            raise_upload_type_error(type_)

        preferred_extension = mimetypes.guess_extension(guessed_mimetype)
        if (
            not (self.filename.lower().endswith(tuple(allowed_extensions)))
            or preferred_extension.lower() not in allowed_extensions
        ):
            raise tk.ValidationError(
                {self.file_field: [f'{self.filename.lower()},{self.filename},{preferred_extension} | Extension error - Only supported file formats are allowed: {", ".join(allowed_extensions)}']}
            )

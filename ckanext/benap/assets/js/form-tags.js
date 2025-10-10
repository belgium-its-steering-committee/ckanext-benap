/*
 * used inside form-tags.html template
 *
 *  on the <input>: 
 *    data-module="form-tags"
 *    data-module-data-field-id="field-{{ field.field_name }}" 
 * With data-field-id the id for the field to store the data
 *
 */
ckan.module('form-tags', function ($) {
  return {
    initialize: function () {
      const dataFieldId= this.options.dataFieldId;
      // target might be out of the scope of this module
      const dataField = $('#'+dataFieldId); 

      // Hide the original data text field
      dataField.hide();

      this.el.change(function () {
        if (this.checked) {
          let tags = dataField.val().split(',');
          tags.push(this.value);
          dataField.val(tags.join().replace(/^,/, ''));
        } else {
          let tags = dataField.val().split(',');
          let remainingTags = [];
          tags.forEach(tag => {
            if (tag.trim() !== this.value) {
              remainingTags.push(tag);
            }
          });
          remainingTags.join();
          dataField.val(remainingTags);
        }
      });
    },
  };
});



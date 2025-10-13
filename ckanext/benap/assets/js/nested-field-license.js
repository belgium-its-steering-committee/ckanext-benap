/*
 * used inside nested-field-license.html template (code is very coupled!)
 *
 *  <div data-module="nested-field-license"></div>
 *
 */

ckan.module('nested-field-license', function ($) {
  return {
    initialize: function () {
      var $conditionsUsageField = $('#field-conditions_usage');
      var $licenseTypeField = $('#field-license_type');
      var $starElement = $('#star');
      var $licenseFieldset = $('#license-fieldset');

      function toggleFieldsetDisability($fieldset, hide) {
        if (hide) {
          $fieldset.hide();
          $fieldset.find('input, select, textarea').each(function () {
            $(this).val('');
          });
        } else {
          $fieldset.show();
        }
      }

      function toggleRequiredFields(toggle) {
        $('#field-license_text_translated-en').prop('required', toggle);
        // option ro make multiple license text fields mandatory
        // $('#field-license_text_translated-en', #field-license_text_translated-nl, #field-license_text_translated-de, #field-license_text_translated-fr').prop('required', toggle);
      }

      $conditionsUsageField.on('change', function () {
        var selectedValue = $(this).val();
        if (
          selectedValue ===
          'https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage/licence-provided'
        ) {
          $licenseTypeField.prop('required', true);
          $starElement.show();
          toggleFieldsetDisability($licenseFieldset, false);
        } else {
          $licenseTypeField.prop('required', false);
          toggleRequiredFields(false);
          $starElement.hide();
          toggleFieldsetDisability($licenseFieldset, true);
        }
      });

      if (
        $conditionsUsageField.val() ===
        'https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage/licence-provided'
      ) {
        $licenseTypeField.prop('required', true);
        $starElement.show();
        toggleFieldsetDisability($licenseFieldset, false);
      } else {
        $licenseTypeField.prop('required', false);
        toggleRequiredFields(false);
        $starElement.hide();
        toggleFieldsetDisability($licenseFieldset, true);
      }

      $licenseTypeField.on('change', function () {
        var licenseTypeValue = $(this).val();
        if (licenseTypeValue === 'Other') {
          toggleRequiredFields(true);
        } else {
          toggleRequiredFields(false);
        }
      });

      if ($licenseTypeField.val() === 'Other') {
        toggleRequiredFields(true);
      } else {
        toggleRequiredFields(false);
      }
    },
  };
});

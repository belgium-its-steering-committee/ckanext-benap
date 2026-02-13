/*
 * used inside nested-field-license.html template (code is very coupled!)
 *
 *  <div data-module="nested-field-license"></div>
 *
 */

ckan.module('nested-field-license', function ($) {
  return {
    initialize: function () {
      const $conditionsUsageField = $('#field-conditions_usage');
      const $licenseTypeField = $('#field-license_type');
      const $asteriskElement = $('#license-asterisk');
      const $licenseFieldset = $('#license-fieldset');
      // Pluck an asterisk from somewhere else on the page, including localized title attribute.
      const $asteriskTemplate = $('span.control-required').first()

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

      function toggleFieldRequired(id, required) {
        if (required) {
          $(`label[for=${id}]`).prepend($asteriskTemplate.clone(), ' ');
        } else {
          $(`label[for=${id}] > .control-required`).remove();
        }
      }

      function toggleRequiredLicenseTextFields(toggle) {
        toggleFieldRequired('field-license_text_translated-en', toggle)
      }

      function updateConditionsForUsage() {
        if (
          $conditionsUsageField.val() ===
          'https://w3id.org/mobilitydcat-ap/conditions-for-access-and-usage/licence-provided'
        ) {
          toggleFieldRequired('field-license_type', true);
          $asteriskElement.show();
          toggleFieldsetDisability($licenseFieldset, false);
        } else {
          toggleFieldRequired('field-license_type', false);
          toggleRequiredLicenseTextFields(false);
          $asteriskElement.hide();
          toggleFieldsetDisability($licenseFieldset, true);
        }
      }

      $conditionsUsageField.on('change', updateConditionsForUsage);
      updateConditionsForUsage();

      function updateLicenseTextField() {
        if ($licenseTypeField.val() === 'Other') {
          toggleRequiredLicenseTextFields(true);
        } else {
          toggleRequiredLicenseTextFields(false);
        }
      }
      $licenseTypeField.on('change', updateLicenseTextField);
      updateLicenseTextField();
    },
  };
});

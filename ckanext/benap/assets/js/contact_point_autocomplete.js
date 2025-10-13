/* Only useable together with the contact_point_with_autocomplete.html template.
Fully coupled via element IDs.
*/
ckan.module('contact-point-autocomplete', function ($) {
  return {
    options: {
      autocomplete_options: [],
      organizations: [],
    },
    initialize: function () {
      const autocompleteOptions = this.options.autocomplete_options;
      const organizations = this.options.organizations;
      let valuesList = Object.values(autocompleteOptions);

      function getOrgEmailAndTelByName(orgs, title) {
        let org = orgs.find((org) => org.title === title);
        return { email: org.do_email, tel: org.do_tel };
      }

      $('#field-contact_point_name').wrap(
        '<div id="autocomplete-contact_point_name"></div>'
      );
      $('#field-contact_point_name').attr('autocomplete', 'off');

      let originalValue = $('#field-contact_point_name').val();
      if (valuesList.includes(originalValue)) {
        $('#field-contact_point_email').prop('readonly', true);
        $('#field-contact_point_tel').prop('readonly', true);
      }

      $('#field-contact_point_name').on('input', function (e) {
        if (e.which !== 40 || e.which !== 38 || e.which !== 13) {
          currentFocus = -1;
          let inputText = this.value;
          if (inputText !== '') {
            $('.autocomplete-contact_point_name-option').remove();
            let matches = autocompleteOptions.filter((x) => {
              return x.toLowerCase().indexOf(inputText.toLowerCase()) > -1;
            });
            matches.sort(function (a, b) {
              return (
                b.toLowerCase().indexOf(inputText.toLowerCase()) <
                a.toLowerCase().indexOf(inputText.toLowerCase())
              );
            });
            if (matches.length > 5) {
              matches = matches.slice(0, 5);
            }
            matches.forEach((m, i) => {
              var $opt = $(
                '<div class="autocomplete-contact_point_name-option border-1" style="top: ' +
                  (i + 1) * 34 +
                  'px;">' +
                  m +
                  '</div>'
              );
              // alternatively use click delegation, but this is closer to the original code
              $opt.on('click', function () {
                selectOption(m);
              });
              $('#autocomplete-contact_point_name').append($opt);
            });
          } else {
            $('.autocomplete-contact_point_name-option').remove();
          }
        }
      });

      function selectOption(selectedValue) {
        $('#field-contact_point_name').val(selectedValue);
        $('.autocomplete-contact_point_name-option').remove();

        if (valuesList.includes(selectedValue)) {
          let orgEmailAndTel = getOrgEmailAndTelByName(
            organizations,
            selectedValue
          );
          $('#field-contact_point_email')
            .val(orgEmailAndTel.email)
            .prop('readonly', true);
          $('#field-contact_point_tel')
            .val(orgEmailAndTel.tel)
            .prop('readonly', true);
        } else {
          $('#field-contact_point_email').val('').prop('readonly', false);
          $('#field-contact_point_tel').val('').prop('readonly', false);
        }
      }

      $('#field-contact_point_name').on('keydown', function (e) {
        let autocompleteOptions = $('.autocomplete-contact_point_name-option');
        if (e.which === 40) {
          // down
          currentFocus++;
          addActive(autocompleteOptions);
          e.preventDefault();
        } else if (e.which === 38) {
          // up
          currentFocus--;
          addActive(autocompleteOptions);
          e.preventDefault();
        } else if (e.which === 13) {
          e.preventDefault();
          if (currentFocus > -1) {
            if (autocompleteOptions) {
              autocompleteOptions[currentFocus].click();
            }
          }
        }
      });

      function addActive(autocompleteOptions) {
        if (!autocompleteOptions) {
          return false;
        }
        removeActive(autocompleteOptions);
        if (currentFocus >= autocompleteOptions.length) {
          currentFocus = 0;
        }
        if (currentFocus < 0) {
          currentFocus = autocompleteOptions.length - 1;
        }
        $(autocompleteOptions[currentFocus]).addClass(
          'autocomplete-contact_point_name-option-active'
        );
      }

      function removeActive(autocompleteOptions) {
        for (var i = 0; i < autocompleteOptions.length; i++) {
          autocompleteOptions[i].classList.remove(
            'autocomplete-contact_point_name-option-active'
          );
        }
      }

      // Add event listener to update the status of related fields when the first field changes
      $('#field-contact_point_name').on('change', function () {
        let selectedValue = $(this).val();

        if (valuesList.includes(selectedValue)) {
          let orgEmailAndTel = getOrgEmailAndTelByName(
            organizations,
            selectedValue
          );
          $('#field-contact_point_email')
            .val(orgEmailAndTel.email)
            .prop('readonly', true);
          $('#field-contact_point_tel')
            .val(orgEmailAndTel.tel)
            .prop('readonly', true);
        } else {
          $('#field-contact_point_email').val('').prop('readonly', false);
          $('#field-contact_point_tel').val('').prop('readonly', false);
        }
      });

      // remove list if clicked outside
      // $(document).click(function() {
      //     $('.autocomplete-contact_point_name-option').remove();
      // });
    },
  };
});

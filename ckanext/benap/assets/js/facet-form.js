/*
 *  Add data-module="facet-form" to a <form> element that wraps facet
 *  checkboxes (see snippets/facet_list.html). Submitting the form reloads
 *  the search page with the checked facet values as url params.
 *  Every change of a checkbox immediately submits the form.
 */
ckan.module('facet-form', function ($) {
  return {
    initialize: function () {
      var form = this.el;
      form.on('change', 'input[type="checkbox"]', function () {
        form[0].submit();
      });
    },
  };
});

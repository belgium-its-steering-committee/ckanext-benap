/*
 * add to any element data-module="hide-control"
 * toggle visibility of provided element id.
 * Uses global selector via id, so doesn't matter where it is set at.
 * Note: this uses a global id getter, because form-controls don't allow
 *  passing data-module to their upper div.
 *   data-module="hide-control"
 *   data-module-hide-id="element id to toggle"
 */
ckan.module('hide-control', function ($) {
  return {
    initialize: function () {
      const hideId = this.options.hideId;
      const targetElement = $('#' + hideId);
      targetElement.toggle();
    }
  };
});

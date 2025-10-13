

/*
 *  add data-module="toggle-section" to an upper element
 *  on the element to add a click handler to toggle the elements: toggle-section-on-click
 *  on the elements that should be toggled: toggle-section-target
 *  on elements to toggle one time at load time: toggle-section-initial-toggle (alternatively add class hide-control)
 */
ckan.module('toggle-section', function ($) {
  return {
    initialize: function () {
      var $onClickTarget = this.el.find('[toggle-section-on-click]');
      var $targets = this.el.find('[toggle-section-target]');
      var $initialToggle = this.el.find('[toggle-section-initial-toggle]');

      $initialToggle.toggle();

      $onClickTarget.on('click', function () {
        $targets.toggle();
      });
    },
  };
});
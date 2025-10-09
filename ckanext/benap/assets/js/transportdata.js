"use strict";

ckan.module("collapsible-section", function ($) {
  return {
    initialize: function () {
      this.isOpen = true;
      this.caret = this._createCaretEl();
      // For some reason the element is wrapped in a singleton list
      this.sectionEl = this.el[0];
      this.headingContainer = this.sectionEl.children[0];
      this.headingContainer.appendChild(this.caret);
      this.headingContainer.style['cursor'] = 'pointer';
      this.collapsiblePart = this.sectionEl.children[1];
      this.headingContainer.addEventListener('mousedown', this._toggleCollapsed.bind(this));
    },
    teardown: function () {
      this.headingContainer.removeEventListener('mousedown', this._toggleCollapsed.bind(this));
    },
    _toggleCollapsed: function () {
      this.isOpen = !this.isOpen;
      if (this.isOpen) {
        this.caret.style['transform'] = 'rotate(180deg)';
        this.collapsiblePart.style['display'] = 'block';
      } else {
        this.caret.style['transform'] = 'rotate(0deg)';
        this.collapsiblePart.style['display'] = 'none';
      }
    },
    _createCaretEl() {
      const caret = document.createElement('span');
      caret.classList = ['category-caret me-3'];
      caret.style['transform'] = 'rotate(180deg)';

      return caret;
    }
  };
});

ckan.module("manage-cookies", function ($) {
  return {
    initialize: function () {
      this.el.on('click', this._openOverlay);
    },
    _openOverlay: function () {
      $('#overlay-cookies').css('display', 'flex');
    }
  };
});

this.ckan.module('benap-select-autocomplete', function($) {
  return {
    initialize() {
      const settings = {
        width: 'resolve',
        matcher(term, text, option) {

          if (!term || term.trim() === '') {
            return !option.data('hidden');
          }

          const re = new RegExp(RegExp.escape(term), 'i');
          if (text.match(re)) {
            return true;
          }

          return null;
        }
      };

      this.el.select2(settings);
      this.el.removeClass('form-select');
      this.el.removeClass('form-control');
    }
  }
})

this.ckan.module('benap-select-autocomplete', function($, _) {
  return {
    initialize() {
      const settings = {
        width: 'resolve',
        placeholder: _('Start typing to search all options'),
        allowClear: true,
        matcher(term, text, option) {

          if (!term || term.trim() === '') {
            return !option.data('hidden');
          }

          const re = new RegExp(RegExp.escape(term), 'i');
          if (text.match(re)) {
            return true;
          }

          return null;
        },
        sorter(items, _el, { term, }) {
          const termRegExp = RegExp.escape(term)
          const re = new RegExp(termRegExp, 'i');
          const startRe = new RegExp(`^${termRegExp}`, 'i');
          const endRe = new RegExp(`${termRegExp}$`, 'i');

          function score(text) {
            if (text.match(startRe)) {
              return 3;
            } else if (text.match(endRe)) {
              return 2;
            } else if (text.match(re)) {
              return 1;
            } else {
              return 0;
            }
          }

          return items.sort(({ text: a }, { text: b }) => {
            const aScore = score(a), bScore = score(b);
            if (aScore === bScore) {
              return a.localeCompare(b);
            } else {
              return bScore - aScore;
            }
          })
        }
      };

      this.el.select2(settings);
      this.el.removeClass('form-select');
      this.el.removeClass('form-control');
    }
  }
})

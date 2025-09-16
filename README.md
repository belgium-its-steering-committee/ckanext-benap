# NAP
Belgium's multimodal transport service catalogue

## Translations
This plugin supports translating strings in its own code as well as overwriting translations provided by core ckan, so faulty translations can be fixed. This can also be used to adjust text (e.g. leave away a sentence) from core ckan templates, without needing to overwrite a template.

Add translatable strings with `{% trans %}text{% endtrans %}` or `_('text')`. See https://docs.ckan.org/en/2.11/contributing/string-i18n.html .


### Adjusting translations
Afterwards, run `./extract_translatable_strings.sh`. This script does the following:
- extract all translatable strings from your plugin code
- *ignore* any strings that ckan core already translates (to avoid extra work)
- insert the translatable strings in the i18n .po files
  - both the strings from the plugin as the ones defined in ckan-translations-overwrite.pot are inserted

The owner of the files might be invalid, so you might need to `chown` the files afterwards.

Afterwards write the translations as needed in the .po files. When done, make sure to run the command `./compile_translations.sh` to compile the .po files to .mo files. Otherwise the translations will not work. In development, you'll need to `bin/reload` the app to see the new translations in effect.

### overwriting ckan core translations
To overwrite translations of ckan core, or from a different plugin, add these inside ckan-translations-overwrite.pot. Add them as `# ` (with a space) and afterwards a comma-separated list of the languages to overwrite (options are `nl`, `fr`, `de` and `en`)
```
# nl,fr,de
msgid "text"
msgstr ""
```

For languages not specified, the msgid will not be added to the .po file and the ckan core translation will be used instead (because of fallback). This is perfect where ckan has a faulty translation in one language, as you can just overwrite that one language and leave the rest intact.

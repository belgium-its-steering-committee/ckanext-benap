# Run to:
# - extra all translatable strings from the benap plugin
# - merge these with custom translations provided in ckan-translations-overwrite.pot
# - update the .po files for every language with the new translations

CKAN_BASE=ckan/ckan-base:2.11
docker run --rm --entrypoint bash -u root -v .:/external "$CKAN_BASE" -lc '
    apt-get -y install gettext
    cd /external
    
    if ! python setup.py extract_messages; then
        echo "!! Error while extracting strings, extraction cancelled. !!"
        exit 1
    fi

    # as ckan does not provide "en" translations, but only "en_GB", make the assmuption it falls back
    # to "en_GB" when the locale is "en". Note: was not explicitely checked.
    LOCALES="nl en_GB de fr"
    LOCALES_PLUGIN="nl en de fr"
    # location of core CKAN translations in ckan-base docker image
    CKAN_I18N_DIR="/srv/app/src/ckan/ckan/i18n"

    PLUGIN_POT="./ckanext/benap/i18n/ckanext-benap.pot"
    OVERWRITE_POT="./ckanext/benap/i18n/ckan-translations-overwrite.pot"
    TMP_ALL_CORE_POT="/tmp/all_lang_core.pot"
    TMP_FILTERED_PLUGIN_POT="/tmp/plugin_filtered.pot"

    ALL_FILES=()
    for lang in $LOCALES; do        
        msgattrib --translated -o "/tmp/${lang}_core.po" "$CKAN_I18N_DIR/$lang/LC_MESSAGES/ckan.po"
        ALL_FILES+=("/tmp/${lang}_core.po")
    done
    msgcomm --more-than=3 "${ALL_FILES[@]}" -o "$TMP_ALL_CORE_POT"

    # unique: only extract translations that are unique to the specified pot files
    # But this will still contain all (unique) ones of ckan core...
    msgcomm --unique "$PLUGIN_POT" "$TMP_ALL_CORE_POT" -o "$TMP_FILTERED_PLUGIN_POT"
    
    # only keep those in both the filtered (translations that existed in just core or just plugin)
    # and plugin => keeps translations in plugin that did not exist in core
    msgcomm --more-than=1 "$PLUGIN_POT" "$TMP_FILTERED_PLUGIN_POT" -o "$TMP_FILTERED_PLUGIN_POT"

    # For each language, only add overwrite entries that specify that language via
    # a comment (line startin with # ) containing this at the start (comma-separated, e.g. `# nl,fr`)
    for lang in $LOCALES_PLUGIN; do
        TMP_OVERWRITE_LANG_POT="/tmp/overwrite_${lang}.pot"
        TMP_MERGED_LANG_POT="/tmp/merged_${lang}.pot"

        # match comment for this language
        msggrep -C -E -e "^((nl|fr|en|de),)*${lang}(,(nl|fr|en|de))*" "$OVERWRITE_POT" -o "$TMP_OVERWRITE_LANG_POT"

        # Merge plugin translation with overwrite (where lang specified in comment)
        xgettext -o "$TMP_MERGED_LANG_POT" "$TMP_FILTERED_PLUGIN_POT" "$TMP_OVERWRITE_LANG_POT"

        # xgettext adds some headers that create a crash. Fix these here, even though they have no meaning in a .pot file
        # alternatively they could be removed?
        sed -i "s/Language: /Language: en/" "$TMP_MERGED_LANG_POT"
        sed -i "s/Plural-Forms: nplurals=INTEGER; plural=EXPRESSION/Plural-Forms: nplurals=2; plural=n != 1/" "$TMP_MERGED_LANG_POT"
        
        # update .po file for this specific language (the filtered plugin translations and overwrites with specified language in comments)
        python setup.py update_catalog --no-fuzzy-matching -i "$TMP_MERGED_LANG_POT" -l "$lang"
    done

    echo "!! make sure to run compile_translations.sh to update the .po files after adjusting the missing translations. !!"
  '
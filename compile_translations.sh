CKAN_BASE=ckan/ckan-base:2.11
docker run --rm --entrypoint bash -u root -v .:/external "$CKAN_BASE" -lc '
    cd /external
    
    if ! python setup.py compile_catalog; then 
        echo "!! Error while compiling translations, compilation cancelled. !!"
        exit 1
    fi
  '
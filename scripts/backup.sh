#! /usr/bin/env bash

docker exec -t cbdt-datastore pg_dumpall -c -U postgres | gzip > ./glbuilds-$(date +%Y-%m-%d).sql.gz

#!/bin/bash
collection=""
if [ ! -z "$1" ]; then
  collection=$1
else
  echo "Usage ./index.sh COLLECTION_NAME"
  exit 1
fi
echo "Indexing data to $collection"
for file in data/*.json; do
  echo $file
  curl "http://localhost:8983/solr/$collection/update" -H 'Content-type:application/json' -d "[`cat $file`]"
  echo
done
curl "http://localhost:8983/solr/$collection/update" -H 'Content-type:application/xml' -d '<commit/>'

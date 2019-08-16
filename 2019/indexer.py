import csv
import copy
import pysolr
import json
import concurrent.futures

def loadJSON(data):
    try:
        raw_desc = json.loads(row[column_index])
        return raw_desc
    except json.decoder.JSONDecodeError:
        return None

solr = pysolr.Solr('http://localhost:8983/solr/shoes')

with open('data.csv') as f:
    readCSV = csv.reader(f, delimiter=',')
    i = 0
    batch = []
    for row in readCSV:
        if i == 0:
            # these are the columns
            columns = row
        else:
            doc={}
            #print(row)
            doc['original_id'] = row[0]
            for column_index in range(1, len(columns)-1):

                '''
                DATA CLEANUP
                '''

                if column_index == len(row):
                    # oops, we got past the end of the document. Break here
                    break
                if columns[column_index] in ['dateAdded', 'dateUpdated', 'prices.dateAdded', 'prices.dateSeen']:
                    if not row[column_index].startswith("20"):
                        # malformed date. Adding a dummy one
                        row[column_index] = '2016-11-11T09:50:34Z'
                if columns[column_index] == 'prices.dateSeen':
                    #keep only the first date, if there are multiple, comma-separated ones
                    row[column_index] = row[column_index].split(",")[0]
                if columns[column_index] == row[column_index]:
                    # dirty data, like ean=ean
                    continue
                if columns[column_index] == 'upc':
                    # this is so dirty, that columns are likely shifted. Break here
                    if not isinstance(row[column_index], (int, float)):
                        break
                if columns[column_index] in ['prices.amountMax', 'prices.amountMin']:
                    # strip dollars
                    if "$" in row[column_index]:
                        row[column_index] = row[column_index].split("$")[1]
                    if not isinstance(row[column_index], (int, float)):
                        continue #give up if it's still not numeric

                '''
                EXTRA PARSING
                '''
                parsed = None
                if columns[column_index] == 'descriptions':
                    parsed = loadJSON(row[column_index])
                    if parsed is not None:
                        desc_text = ''
                        for description in parsed:
                            desc_text = desc_text + description['value'] + ' '
                        doc[columns[column_index]] = desc_text

                if columns[column_index] == 'features':
                    parsed = loadJSON(row[column_index])
                    if parsed is not None:
                        for feature in parsed:
                            doc[feature['key']] = feature['value']

                if columns[column_index] == 'skus':
                    parsed = loadJSON(row[column_index])
                    if parsed is not None:
                        doc['skus'] = []
                        for sku in parsed:
                            doc['skus'] = sku['value']

                if columns[column_index] == 'reviews':
                    parsed = loadJSON(row[column_index])
                    if parsed is not None:
                        doc['reviews'] = []
                        for review in parsed:
                            try:
                                doc['reviews'] = review['text']
                            except KeyError:
                                pass # no text in this review, we'll pass (pun intended)

                if columns[column_index] == 'merchants':
                    parsed = loadJSON(row[column_index])
                    if parsed is not None:
                        doc['merchants'] = []
                        for merchant in parsed:
                            doc['merchants'].append(merchant['name'])

                if parsed is None:
                    doc[columns[column_index]] = row[column_index]
            batch.append(copy.deepcopy(doc))
            #print(doc)
        if len(batch) > 500: #batch size
            #print(batch)
            solr.add(batch)
            batch=[]
            print(i)
        #if i == 15:
        #    break
        i += 1

# send whatever is left
solr.add(batch)
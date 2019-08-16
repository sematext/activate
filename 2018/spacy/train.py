# python code (train.py)

from __future__ import unicode_literals
import spacy
import random

DATA = [
        (u"Search Analytics: Business Value & BigData NoSQL Backend, Otis Gospodnetic ", {'entities': [ (58,75,'PERSON') ] }),
        (u"Introduction to Elasticsearch by Radu ", {'entities': [ (16,29,'TECH'), (32, 36, 'PERSON') ] }),
        (u"Monitorama EU 2013 - Radu Gheorghe ", {'entities': [ (0,10,'CONF'), (14,18,'DATE'), (21,33,'PERSON') ] }),
        (u"#bbuzz: Rafal Kuc: Battle of the Giants: Solr vs ElasticSearch, Round 2 ", {'entities': [ (8,17,'PERSON'), (41,45,'TECH'), (49,62,'TECH') ] }),
        (u"Understanding & Visualising Solr EXPLAIN Information, Rafal Kuc ", {'entities': [ (29,33,'TECH'), (54,63,'PERSON') ] }),
        (u"Scaling Solr with SolrCloud , Rafal Kuc, Sematext ", {'entities': [ (8,12,'TECH'), (18,27,'TECH'), (30,39,'PERSON'), (41,49,'COMPANY') ] }),
        (u"Solr for Analytics: Metrics Aggregations at Sematext Otis Gospodnetic ", {'entities': [ (0,4,'TECH'), (44,52,'COMPANY'), (54,70,'PERSON') ] }),
        (u"Battle of the giants: Apache Solr 4.0 vs ElasticSearch ", {'entities': [ (29,33,'TECH'), (34,37,'VERSION'), (41,54,'TECH') ] }),
        (u"Using Solr to Search and Analyze Logs, Radu Gheorghe ", {'entities': [ (6,10,'TECH'), (39,52,'PERSON') ] })
]


nlp = spacy.blank('en')
nlp.vocab.vectors.name = 'example_model_training'

# add NER pipeline
ner = nlp.create_pipe('ner')
nlp.add_pipe(ner, last=True)

# add entity names used in training data
nlp.entity.add_label('PERSON')
nlp.entity.add_label('TECH')
nlp.entity.add_label('CONF')
nlp.entity.add_label('VERSION')
nlp.entity.add_label('COMPANY')
nlp.entity.add_label('DATE')

optimizer = nlp.begin_training()

for i in range(20):
	random.shuffle(DATA)
	for text, annotations in DATA:
		nlp.update([text], [annotations], sgd=optimizer)

print("")
print("Doc 10, title: '#bbuzz: Radu Gheorghe JSON Logging with Elasticsearch'")
print("-----")
doc = nlp(u"#bbuzz: Radu Gheorghe JSON Logging with Elasticsearch")
for entity in doc.ents:
  print(entity.label_, ' | ', entity.text)

print("")
print("Doc 20:, title: 'How to Run Solr on Docker. And Why. - Rafał Kuć & Radu Gheorghe, Sematext'")
print("-----")
doc = nlp(u"How to Run Solr on Docker. And Why. - Rafał Kuć & Radu Gheorghe, Sematext")
for entity in doc.ents:
  print(entity.label_, ' | ', entity.text)

print("")
print("Doc 37:, title: '#bbuzz 2016: Rafał Kuć - Running High Performance And Fault Tolerant Elasticsearch'")
print("-----")
doc = nlp(u"#bbuzz 2016: Rafał Kuć - Running High Performance And Fault Tolerant Elasticsearch")
for entity in doc.ents:
  print(entity.label_, ' | ', entity.text)

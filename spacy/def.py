from __future__ import unicode_literals
import spacy

nlp = spacy.load('en_core_web_sm')

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

wget http://www-eu.apache.org/dist/opennlp/opennlp-1.9.0/apache-opennlp-1.9.0-bin.tar.gz
tar zxf apache-opennlp-1.9.0-bin.tar.gz

cp * apache-opennlp-1.9.0/ 2>/dev/null

cd apache-opennlp-1.9.0

wget http://opennlp.sourceforge.net/models-1.5/en-ner-date.bin
wget http://opennlp.sourceforge.net/models-1.5/en-ner-organization.bin

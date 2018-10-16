import gensim

class GenWords(object):
    def __init__(self, filename):
        self.filename = filename

    def __iter__(self):
        for line in open(self.filename):
            yield line.lower().split()

words = GenWords('videos')

# can tune things, may parallelize, etc; would be faster with C compiler before installing Gensim
print("Training the model...")
model = gensim.models.Word2Vec(words,
                               min_count=5,
                               window=5,
                               iter=5000) # default iter=5; small dataset

print("\nSynonyms with Youtube:")
print(model.most_similar("youtube"))

print("\nSynonyms with Solr:")
print(model.most_similar("solr"))

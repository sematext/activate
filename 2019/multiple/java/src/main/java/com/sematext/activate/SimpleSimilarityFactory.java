package com.sematext.activate;

import org.apache.lucene.search.similarities.IndependenceStandardized;
import org.apache.lucene.search.similarities.Similarity;
import org.apache.solr.common.params.SolrParams;
import org.apache.solr.schema.SimilarityFactory;

public class SimpleSimilarityFactory extends SimilarityFactory {
  private volatile Similarity similarity;

  public void init(SolrParams params) {
    super.init(params);
  }

  public Similarity getSimilarity() {
    if (similarity == null) {
      similarity = new SimpleSimilarity(new IndependenceStandardized());
    }
    return similarity;
  }
}

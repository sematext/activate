package com.sematext.activate;

import org.apache.lucene.index.FieldInvertState;
import org.apache.lucene.search.CollectionStatistics;
import org.apache.lucene.search.TermStatistics;
import org.apache.lucene.search.similarities.Similarity;

public class SimpleSimilarity extends Similarity {
  public SimpleSimilarity() {}

  public long computeNorm(FieldInvertState state) { return 1; }

  public Similarity.SimScorer scorer(float boost,
      CollectionStatistics collectionStats, TermStatistics... termStats) {
    return new SimpleSimScorer();
  }
}

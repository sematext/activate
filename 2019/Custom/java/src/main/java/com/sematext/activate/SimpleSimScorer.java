package com.sematext.activate;

import org.apache.lucene.search.similarities.Similarity;

public class SimpleSimScorer extends Similarity.SimScorer {
  public float score(float freq, long norm) {
    return freq;
  }
}

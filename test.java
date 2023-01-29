//quote price size side
//getTopask
//gettopbid
//collection of top asks and top bids


Class Quote {
  Class enum Side {bid, ask };

  private double px;
  private long size;
  private Side side;

  public Quote(double px, long size, Side side) {
    this.px = px;
    this.size = size;
    this.side = side;
  }
}

class Book {
  private List<Quote> asks = new ArryList<>();
  private List<Quote> bids = new ArrayList<>();

  //  11, 6, 3 2
  public void addBid(Quote bid) {
    int i = 0;
    boolean inserted = false;

    while (i < bids.size()) {
      if (bid.px >= bids[i].px) {
          bids.insert(i, bid)
          inserted = true;
          break;

      }
      i += 1;
    }

    if (!inserted) {
      this.bids.add(bid)
    }
  }

  public void addAsk(Quote ask) {
    int i = 0;

    if (this.asks.size() == 0) {
      this.asks.add(ask)
      return;
    }

    while (i < asks.size()) {
      if (ask.px <= asks[i].px) {
          bids.insert(i, ask)
          break;
      }
      i += 1;
    }
  }

  public Quote getTopBid() {
    return this.bids.size() != 0 ? bids[0] : null;
  }

  public Quote getTopAsk() {
    return this.asks.size() != 0 ? asks[0] : null;
  }

  public List<Quote> getAllTopBids(int n) {
      List<Quote> topNBids = new ArrayList<>();

      for (int i = 0; i < n; i ++) {
        topNBids.add(this.bids[i]);
      }

      return topNBids;
  }

  public List<Quote> getAllTopAsks(int n) {
      List<Quote> topNAsks = new ArrayList<>();

      for (int i = 0; i < n; i ++) {
        topNAsks.add(this.asks[i]);
      }

      return topNAsks;
  }






}

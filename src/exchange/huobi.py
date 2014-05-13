#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import json

from util import crawl, data

def __akey(x): return x[0]

def get_depth(url):
  """
  >>> data.is_valid_depth(get_depth('http://market.huobi.com/staticmarket/detail_ltc_json.js'))
  True
  """
  jdata = crawl.get_jason_from_url(url)
  if 'buys' in jdata and 'sells' in jdata:
    bids, asks = [], []
    for buy in jdata['buys']:
      bids.append((float(buy['price']),float(buy['amount'])))
    for sell in jdata['sells']:
      asks.append((float(sell['price']),float(sell['amount'])))

    bids.sort(key=__akey, reverse=True)
    asks.sort(key=__akey)
    return (bids, asks)

def get_btc_cny_depth():
  """
  >>> data.is_valid_goodsrate(get_btc_cny_depth())
  True
  """
  return ('huobi', 'btc-cny', get_depth('http://market.huobi.com/staticmarket/detail_btc_json.js'))

def get_ltc_cny_depth():
  """
  >>> data.is_valid_goodsrate(get_ltc_cny_depth())
  True
  """
  return ('huobi', 'ltc-cny', get_depth('http://market.huobi.com/staticmarket/detail_ltc_json.js'))

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

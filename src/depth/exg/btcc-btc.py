#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, os, sys, urllib.request

sys.path.append(os.path.expanduser('~/src/util'))
from util import *

shortname = 'CC'
longname = 'BTCChina'

def akey(x): return x[0]

def get_depth():
  """
  >>> x = get_depth()
  >>> is_valid_goodsrate(x)
  True
  """
  jdata = get_jason_from_url('https://data.btcchina.com/data/orderbook')
  if 'asks' in jdata and 'bids' in jdata:
    jdata['bids'].sort(key=akey, reverse=True)
    jdata['asks'].sort(key=akey)
    return ('BTC-CNY', (jdata['bids'], jdata['asks']))

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

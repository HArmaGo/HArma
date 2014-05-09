#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import json, os, sys, urllib.request

sys.path.append(os.path.expanduser('../util'))
from inc import *

def akey(x): return x[0]

def get_btc_cny_depth():
  """
  >>> x = get_btc_cny_depth()
  >>> is_valid_goodsrate(x)
  True
  """
  jdata = get_jason_from_url('https://data.btcchina.com/data/orderbook')
  if 'asks' in jdata and 'bids' in jdata:
    jdata['bids'].sort(key=akey, reverse=True)
    jdata['asks'].sort(key=akey)
    return ('btc-cny', (jdata['bids'], jdata['asks']))

def get_ltc_btc_depth():
  """
  >>> x = get_ltc_btc_depth()
  >>> is_valid_goodsrate(x)
  True
  """
  jdata = get_jason_from_url('https://data.btcchina.com/data/orderbook?market=ltcbtc')
  if 'asks' in jdata and 'bids' in jdata:
    jdata['bids'].sort(key=akey, reverse=True)
    jdata['asks'].sort(key=akey)
    return ('ltc-btc', (jdata['bids'], jdata['asks']))

def get_ltc_cny_depth():
  """
  >>> x = get_ltc_cny_depth()
  >>> is_valid_goodsrate(x)
  True
  """
  jdata = get_jason_from_url('https://data.btcchina.com/data/orderbook?market=ltccny')
  if 'asks' in jdata and 'bids' in jdata:
    jdata['bids'].sort(key=akey, reverse=True)
    jdata['asks'].sort(key=akey)
    return ('ltc-cny', (jdata['bids'], jdata['asks']))

def get_depth():
  """
  >>> x = get_depth()
  >>> all([is_valid_goodsrate(y) for y in x])
  True
  """
  res = []
  try: res.append(get_ltc_btc_depth())
  except: print(traceback.format_exc())
  try: res.append(get_btc_cny_depth())
  except: print(traceback.format_exc())
  try: res.append(get_ltc_cny_depth())
  except: print(traceback.format_exc())
  return res

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

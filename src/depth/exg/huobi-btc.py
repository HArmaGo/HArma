#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, os, sys, urllib.request

sys.path.append(os.path.expanduser('~/src/util'))
from util import *

shortname = 'HB'
longname = 'Huobi'

def akey(x): return x[0]

def get_depth():
  """
  >>> x = get_depth()
  >>> is_valid_goodsrate(x)
  True
  """
  jason = get_jason_from_url('http://market.huobi.com/staticmarket/detail_btc_json.js')
  if not jason: self.__raise('no jason')
  if 'code' in jason: self.__check_code(str(jason['code']))
  if not 'buys' in jason or not 'sells' in jason: self.__raise('no buys/sells')
  bids, asks = [], []
  for buy in jason['buys']:
    if not 'amount' in buy or not 'price' in buy: self.__raise('no amount/price')
    bids.append((float(buy['price']),float(buy['amount'])))
  for sell in jason['sells']:
    if not 'amount' in sell or not 'price' in sell: self.__raise('no amount/price')
    asks.append((float(sell['price']),float(sell['amount'])))
  if len(bids) == 0 or len(asks) == 0: self.__raise('empty bids/asks')

  jdata = {}
  jdata['bids'] = bids
  jdata['asks'] = asks

  if 'asks' in jdata and 'bids' in jdata:
    jdata['bids'].sort(key=akey, reverse=True)
    jdata['asks'].sort(key=akey)
    return ('BTC-CNY', (jdata['bids'], jdata['asks']))

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

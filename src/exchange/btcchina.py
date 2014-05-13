#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from util import data
from exchange import common

def get_btc_cny_depth():
  """
  >>> data.is_valid_goodsrate(get_btc_cny_depth())
  True
  """
  return ('btcchina', 'btc-cny', common.get_depth('https://data.btcchina.com/data/orderbook'))

def get_ltc_btc_depth():
  """
  >>> data.is_valid_goodsrate(get_ltc_btc_depth())
  True
  """
  return ('btcchina', 'ltc-btc', common.get_depth('https://data.btcchina.com/data/orderbook?market=ltcbtc'))

def get_ltc_cny_depth():
  """
  >>> data.is_valid_goodsrate(get_ltc_cny_depth())
  True
  """
  return ('btcchina', 'ltc-cny', common.get_depth('https://data.btcchina.com/data/orderbook?market=ltccny'))

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

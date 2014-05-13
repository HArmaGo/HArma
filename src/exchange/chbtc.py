#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from util import data
from exchange import common

def get_btc_cny_depth():
  """
  >>> data.is_valid_goodsrate(get_btc_cny_depth())
  True
  """
  return ('chbtc', 'btc-cny', common.get_depth('http://api.chbtc.com/data/depth'))

def get_ltc_cny_depth():
  """
  >>> data.is_valid_goodsrate(get_ltc_cny_depth())
  True
  """
  return ('chbtc', 'ltc-cny', common.get_depth('http://api.chbtc.com/data/ltc/depth'))

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

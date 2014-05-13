#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from util import data
from exchange import common

def get_nothing(): pass

def get_btc_cny_depth():
  """
  >>> data.is_valid_goodsrate(get_btc_cny_depth())
  True
  """
  return ('okcoin', 'btc-cny', common.get_depth('http://www.okcoin.com/api/depth.do'))

def get_ltc_cny_depth():
  """
  >>> data.is_valid_goodsrate(get_ltc_cny_depth())
  True
  """
  return ('okcoin', 'ltc-cny', common.get_depth('http://www.okcoin.com/api/depth.do?symbol=ltc_cny'))

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

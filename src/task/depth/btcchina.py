#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from exchange import btcchina
from task.depth import common

def task():
  """
  >>> task()
  """
  funcs = [ btcchina.get_btc_cny_depth, \
            btcchina.get_ltc_cny_depth, \
            btcchina.get_ltc_btc_depth ]
  common.do_get_depth_task(funcs)

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

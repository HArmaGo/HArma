#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from exchange import huobi
from task.depth import common

def task():
  """
  >>> task()
  """
  funcs = [ huobi.get_btc_cny_depth, \
            huobi.get_ltc_cny_depth ]
  common.do_get_depth_task(funcs)

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

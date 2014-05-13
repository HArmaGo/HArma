#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import json, os, time 

from util import dump

last = {}
record = {}

def do_get_depth_task(funcs):
  """
  >>> from exchange import okcoin
  >>> do_get_depth_task([ okcoin.get_btc_cny_depth, okcoin.get_nothing ]) \
      #doctest: +ELLIPSIS
  [...] Exception 0:
  Traceback (most recent call last):
   ...
  TypeError: ...
  """
  for func in funcs:
    try:
      rate = func()
      exgname, ratename, (bids, asks) = func()
      depthStr = json.dumps((bids[:10], asks[:10]))

      if exgname not in last: last[exgname] = {}
      if ratename not in last[exgname] or last[exgname][ratename] != depthStr:
        last[exgname][ratename] = depthStr
        dump.dump_log(os.path.join('depth', ratename, exgname), depthStr)

        if exgname not in record: record[exgname] = {}
        if ratename not in record[exgname]: record[exgname][ratename] = [ time.time(), 0 ]
        record[exgname][ratename] = record[exgname][ratename] + 1
        if time.time() - record[exgname][ratename][0] > 600:
          line = '%d %s depth updates from %s in the last %.0f seconds' \
                 %(record[exgname][ratename][1], ratename, exgname, \
                   time.time() - record[exgname][ratename][0])
          record[exgname][ratename] = [ time.time(), 0 ]
          dump.dump_log_and_print('depth', line)
    except:
      dump.dump_exception('depth')

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

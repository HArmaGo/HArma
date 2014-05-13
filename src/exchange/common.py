#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

from util import crawl, data

def __akey(x): return x[0]

def get_depth(url):
  """
  >>> data.is_valid_depth(get_depth('http://www.okcoin.com/api/depth.do'))
  True
  """
  jdata = crawl.get_jason_from_url(url)
  if 'bids' in jdata and 'asks' in jdata:
    jdata['bids'].sort(key=__akey, reverse=True)
    jdata['asks'].sort(key=__akey)
    return (jdata['bids'], jdata['asks'])

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

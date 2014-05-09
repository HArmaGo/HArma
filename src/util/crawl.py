#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import json, urllib.request

def get_jason_from_url(url):
  """
  >>> x = get_jason_from_url('http://www.okcoin.com/api/depth.do')
  >>> len(x) > 0
  True
  """
  res = urllib.request.urlopen(url)
  data = res.read()
  txt = data.decode('utf-8')
  jdata = json.loads(txt)
  return jdata

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

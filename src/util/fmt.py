#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import time

def get_date(t = -1): # do not write t = time.time(), evaluate once
  """
  >>> x = get_date()
  >>> int(x[0:4]) > 2000 and int(x[0:4]) < 2099 and int(x[5:7]) >= 1 and \
      int(x[5:7]) <= 12 and int(x[8:10]) >= 1 and int(x[8:10]) <= 31
  True
  """
  if t == -1: t = time.time()
  return time.strftime('%Y-%m-%d', time.localtime(t))

def get_time(t = -1): # do not write t = time.time(), evaluate once
  """
  >>> x = get_time()
  >>> int(x[0:2]) >= 0 and int(x[0:2]) <= 23 and int(x[3:5]) >= 0 and \
      int(x[3:5]) <= 59 and int(x[6:8]) >= 0 and int(x[6:8]) <= 59
  True
  """
  if t == -1: t = time.time()
  return time.strftime('%X', time.localtime(t))

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import json, os

def get_normal_path(path):
  """
  >>> get_normal_path('$HArmaRoot/a/../b//c/')
  '/home/HArma/b/c'
  """
  path = os.path.expanduser(path)
  path = os.path.expandvars(path)
  path = os.path.abspath(path)
  path = os.path.normpath(path)
  return path

def load_cfg_field(path, field):
  """
  >>> x = load_cfg_field('$HArmaRoot/src/cfg', 'queueSize')
  >>> x > 0
  True
  """
  path = get_normal_path(path)
  with open(path, 'r', encoding =  'utf-8') as myFile:
    lines = ' '.join( l[:-1] for l in myFile.readlines() )
    jdata = json.loads(lines)
    assert field in jdata
    return jdata[field]

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

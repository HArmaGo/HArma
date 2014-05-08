#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, os, shutil

def get_working_dir():
  """
  >>> x = get_working_dir()
  >>> x.count('HArma') > 0
  True
  """
  rpath = os.path.expanduser('~/')
  return rpath

def setup_dir(path):
  """
  >>> dx = './asdklfjklasdfjkl'
  >>> x = '%s/a/b/c/d' %dx
  >>> os.path.exists(x)
  False
  >>> setup_dir(x)
  >>> os.path.exists(x)
  True
  >>> shutil.rmtree(dx)
  """
  if not os.path.exists(path):
    os.makedirs(path)

def load_cfg_field(path, field):
  """
  >>> x = load_cfg_field('../depth/cfg', 'exchanges')
  >>> len(x) > 0
  True
  """
  with open(path, 'r', encoding = 'utf-8') as myFile:
    lines = ' '.join( l[:-1] for l in myFile.readlines() )
    jdata = json.loads(lines)
    assert field in jdata
    return jdata[field]

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import json, os, shutil

def get_working_dir():
  """
  >>> x = get_working_dir()
  >>> x.count('HArma') > 0
  True
  """
  absPath = os.path.expanduser('~/')
  return absPath

def setup_dir(path):
  """
  >>> dx = './asdklfjklasdfjkl'
  >>> x = '%s/a/b/c/d' %dx
  >>> setup_dir(x)
  >>> os.path.exists(x)
  True
  >>> shutil.rmtree(dx)
  """
  absPath = os.path.abspath(path)
  if not os.path.exists(absPath):
    os.makedirs(absPath)

def load_cfg_field(path, field):
  """
  >>> x = load_cfg_field('../depth/cfg', 'exchanges')
  >>> len(x) > 0
  True
  """
  absPath = os.path.abspath(path)
  with open(absPath, 'r') as myFile:
    lines = ' '.join( l[:-1] for l in myFile.readlines() )
    jdata = json.loads(lines)
    assert field in jdata
    return jdata[field]

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import os, sys, traceback

sys.path.append('util')
from inc import *

def parse_module_path(mPath):
  """
  >>> x = parse_module_path('./depth/zealot.py')
  >>> x[0] #doctest: +ELLIPSIS
  '...depth'
  >>> x[1]
  'zealot'
  """
  absPath = os.path.abspath(mPath)
  assert os.path.isfile(absPath)
  head = os.path.dirname(absPath)
  tail = os.path.basename(absPath)
  tail = os.path.splitext(tail)[0]
  return head, tail

def start_module(module, path):
  """
  >>> threading.Thread(target=__test1).start()
  >>> start_module('zealot', './depth') #doctest: +ELLIPSIS
  [...] thread main created.
  [...] thread worker created.
  [...] thread main loaded.
  [...] thread worker terminated.
  [...] thread main terminated.
  """
  reg_exit_signal()
  reg_reload_signal()

  try:
    rpath = os.path.abspath(path)
    sys.path.append(rpath)

    os.chdir(rpath)
    mod = __import__(module)
    mod.main()
  except:
    print(traceback.format_exc())

def __test1():
  """
  >>> __test1()
  >>> pop_flag('exit')
  True
  """
  set_flag('exit')

if __name__ == '__main__':
  if len(sys.argv) != 2:
    import doctest
    print (doctest.testmod())
    print('Usage: %s [ModulePath]' % sys.argv[0])
  else:
    path, module = parse_module_path(sys.argv[1])
    start_module(module, path)

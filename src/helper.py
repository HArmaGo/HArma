#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os, sys, traceback

sys.path.append(os.path.expanduser('~/src/util'))
from util import *

if __name__ == '__main__':
  if len(sys.argv) != 3:
    print('Usage: %s [Path] [Module]' % sys.argv[0])
    exit()

  reg_exit_signal()
  reg_reload_signal()

  path, module = sys.argv[1], sys.argv[2]
  try:
    rpath = os.path.abspath(path)
    os.chdir(rpath)
    sys.path.append(rpath)
    mod = __import__(module)
    mod.main()
  except:
    print(traceback.format_exc())


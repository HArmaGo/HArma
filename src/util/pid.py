#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import os

from util import wdir

def create_pid_file(module):
  """
  >>> x = os.path.expandvars('$HArmaRoot/var/test.pid')
  >>> if os.path.exists(x): os.remove(x)
  >>> create_pid_file('test')
  >>> os.path.exists(x)
  True
  >>> x = os.remove(x)
  """
  path = wdir.get_normal_path(os.path.join('$HArmaRoot/var', module + '.pid'))
  with open(path, 'w', encoding = 'utf-8') as myFile:
    myFile.write('%d' %os.getpid())

def remove_pid_file(module):
  """
  >>> x = os.path.expandvars('$HArmaRoot/var/test.pid')
  >>> y = os.mknod(x)
  >>> os.path.exists(x)
  True
  >>> remove_pid_file('test')
  >>> os.path.exists(x)
  False
  """
  path = wdir.get_normal_path(os.path.join('$HArmaRoot/var', module + '.pid'))
  os.remove(path)

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

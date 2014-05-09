#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import os, shutil

import fmt, wdir

def dump_log_and_print(path, line):
  """
  >>> date = fmt.get_date()
  >>> dx = '../../trash/asdklfjklasdfjkl'
  >>> dx = os.path.abspath(dx)
  >>> x = '%s/a/b/c/d' %dx
  >>> y = '%s/%s.log' %(x, date)
  >>> dump_log_and_print(x, 'a') #doctest: +ELLIPSIS
  [...] a
  >>> shutil.rmtree(dx)
  """
  print ('[%s %s] %s' %(fmt.get_date(), fmt.get_time(), line))
  dump_log(path, line)

def dump_log(path, line):
  """
  >>> date = fmt.get_date()
  >>> dx = '../../trash/asdklfjklasdfjkl'
  >>> dx = os.path.abspath(dx)
  >>> x = '%s/a/b/c/d' %dx
  >>> y = '%s/%s.log' %(x, date)
  >>> dump_log(x, 'a')
  >>> with open(y, 'r', encoding = 'utf-8') as myFile:
  ...   for line in myFile.readlines():
  ...     print(line[11:-1])
  a
  >>> shutil.rmtree(dx)
  """
  path = os.path.join(wdir.get_working_dir(), 'log', path) 
  wdir.setup_dir(path)
  date = fmt.get_date()
  fname = '%s/%s.log' %(path, date)
  with open(fname, 'a', encoding = 'utf-8') as myFile:
    myFile.write('[%s] %s\n' %(fmt.get_time(), line))

def dump_logs_and_print(path, lines):
  """
  >>> date = fmt.get_date()
  >>> dx = '../../trash/asdklfjklasdfjkl'
  >>> dx = os.path.abspath(dx)
  >>> x = '%s/a/b/c/d' %dx
  >>> y = '%s/%s.log' %(x, date)
  >>> dump_logs_and_print(x, [ 'a', 'b' ]) #doctest: +ELLIPSIS
  [...] a
  [...] b
  >>> shutil.rmtree(dx)
  """
  for line in lines:
    dump_log_and_print(path, line)

def dump_logs(path, lines):
  """
  >>> date = fmt.get_date()
  >>> dx = '../../trash/asdklfjklasdfjkl'
  >>> dx = os.path.abspath(dx)
  >>> x = '%s/a/b/c/d' %dx
  >>> y = '%s/%s.log' %(x, date)
  >>> dump_logs(x, ['a', 'b'])
  >>> with open(y, 'r', encoding = 'utf-8') as myFile:
  ...   for line in myFile.readlines():
  ...     print(line[11:-1])
  a
  b
  >>> shutil.rmtree(dx)
  """
  for line in lines:
    dump_log(path, line)

def dump_exception(path, lines):
  path = os.path.join(wdir.get_working_dir(), 'exception', path) 
  pass

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

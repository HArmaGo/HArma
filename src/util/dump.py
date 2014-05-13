#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import os, shutil, time, traceback

import util.fmt as fmt
import util.wdir as wdir

def __test1(firstStep):
  """
  >>> __test1(True)
  'asdkasdffads/a/b/c/d'
  >>> __test1(False) #doctest: +IGNORE_EXCEPTION_DETAIL
  Traceback (most recent call last):
  FileNotFoundError: message
  'asdkasdffads/a/b/c/d'
  """
  rx = 'asdkasdffads'
  ry = os.path.join(rx, 'a/b/c/d')
  rz = os.path.join(ry, '%s.log' %fmt.get_date())
  x = wdir.get_normal_path(os.path.join('$HArmaRoot/log', rx))
  z = wdir.get_normal_path(os.path.join('$HArmaRoot/log', rz))
  if not firstStep:
    with open(z, 'r', encoding = 'utf-8') as myFile:
      for line in myFile.readlines():
        print(line[:-1])
  if os.path.exists(x):
    shutil.rmtree(x)
  if firstStep:
    return ry
  
def dump_log(rPath, line):
  """
  >>> dump_log(__test1(True), 'a')
  >>> __test1(False) #doctest: +ELLIPSIS
  [...] a
  """
  path = wdir.get_normal_path(
         os.path.join('$HArmaRoot/log', rPath, '%s.log' %fmt.get_date()))

  if not os.path.exists(os.path.dirname(path)):
    os.makedirs(os.path.dirname(path))

  with open(path, 'a', encoding = 'utf-8') as myFile:
    myFile.write('[%s] %s\n' %(fmt.get_time(), line))

def dump_logs(rPath, lines):
  """
  >>> dump_logs(__test1(True), ['a','b'])
  >>> __test1(False) #doctest: +ELLIPSIS
  [...] a
  [...] b
  """
  [ dump_log(rPath, line) for line in lines ]

def dump_log_and_print(rPath, line):
  """
  >>> dump_log_and_print(__test1(True), 'a') #doctest: +ELLIPSIS
  [...] a
  >>> __test1(False) #doctest: +ELLIPSIS
  [...] a
  """
  print ('[%s %s] %s' %(fmt.get_date(), fmt.get_time(), line))
  dump_log(rPath, line)

def dump_logs_and_print(rPath, lines):
  """
  >>> dump_logs_and_print(__test1(True), ['a','b']) #doctest: +ELLIPSIS
  [...] a
  [...] b
  >>> __test1(False) #doctest: +ELLIPSIS
  [...] a
  [...] b
  """
  [ dump_log_and_print(rPath, line) for line in lines ]

exps = {}
def dump_exception(rPath):
  """
  >>> for i in range(2): #doctest: +ELLIPSIS
  ...   try: x
  ...   except: dump_exception('test')
  [...] Exception 0:
  Traceback (most recent call last):
   ...
  NameError: ...
  >>> os.path.exists(os.path.expandvars( \
        os.path.join('$HArmaRoot/log/exception/test', '%s.log' %fmt.get_date())))
  True
  >>> shutil.rmtree(os.path.expandvars('$HArmaRoot/log/exception/test'))
  """
  msg = traceback.format_exc()
  if msg in exps:
    if time.time() - exps[msg][1] > 300:
      if exps[msg][2] > 0:
        line = 'Exception %d (and %d times in the last %.0f seconds)' \
               %(exps[msg][0], exps[msg][2], time.time()-exps[msg][1])
      else:
        line = 'Exception %d' %exps[msg][0]
      exps[msg][1], exps[msg][2] = time.time(), 1
      dump_log_and_print(os.path.join('exception', rPath), line)
    else:
      exps[msg][2] = exps[msg][2] + 1
  else:
    exps[msg] = [ len(exps), time.time(), 0 ]
    line = 'Exception %d:\n%s' %(exps[msg][0], msg)
    dump_log_and_print(os.path.join('exception', rPath), line)

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

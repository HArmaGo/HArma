#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json, os, sys, threading, time, traceback

sys.path.append(os.path.expanduser('~/src/util'))
from util import *

exgList = {}
thPool = []
taskQue = que(1)

def load_exg(name):
  """
  >>> exg = load_exg('okcoin-btc')
  """
  sys.path.append(os.path.expanduser('~/src/depth/exg'))
  return __import__(name)

def wait_all():
  """
  >>> wait_all() #doctest: +ELLIPSIS
  [...] thread worker terminated.
  """
  set_flag('exit_worker')
  if len(thPool) > 0:
    for th in thPool:
      th.join()
    dump_log_and_print ('depth', 'thread worker terminated.')
  pop_flag('exit_worker')

def load():
  """
  >>> load() #doctest: +ELLIPSIS
  [...] thread worker created.
  """
  global exgList, thPool, taskQue

  # wait all threads
  wait_all()

  # setup exchanges
  exgList = {}
  exgs = load_cfg_field('./cfg', 'exchanges')
  for exg in exgs:
    name, prd = exg['exchange'], float(exg['period'])
    exgList[name] = [ load_exg(name), prd, 0, None ]

  # clear queue
  qSize = load_cfg_field('./cfg', 'queueSize')
  taskQue = que(qSize)

  # start all threads
  thPool = [ threading.Thread(target=worker) for i in range(qSize) ]
  for th in thPool:
    th.start()
  dump_log_and_print ('depth', 'thread worker created.')

def update(exg, d):
  """
  """
  mod, _, _, data = exgList[exg]
  name, depth = d[0], (d[1][0][:10], d[1][1][:10])
  if data != depth:
    path, line = 'depth/' + name + '/' + mod.longname, json.dumps(depth)
    dump_log(path, line)
    exgList[exg][3] = depth

def __test1(flag):
  time.sleep(0.5)
  set_flag(flag)

def __test2():
  global thPool
  thPool = []

def worker():
  """
  >>> threading.Thread(target=__test1, args=('exit_worker',)).start()
  >>> worker()
  """
  while not get_flag('exit_worker'):
    try:
      exg = taskQue.pop()
      if exg:
        assert exg in exgList
        mod, _, _, data = exgList[exg]
        exgList[exg][2] = time.time()
        #dump_log_and_print('depth', 'pick %s on %s' %(exg, time.time()))

        update(exg, mod.get_depth())
        #dump_log_and_print('depth', 'got  %s on %s' %(exg, time.time()))
      else:
        time.sleep(0.011)
    except:
      print(traceback.format_exc())
    
def main():
  """
  >>> __test2()
  >>> threading.Thread(target=__test1, args=('exit',)).start()
  >>> main() #doctest: +ELLIPSIS
  [...] thread main created.
  [...] thread worker created.
  [...] thread main loaded.
  [...] thread worker terminated.
  [...] thread main terminated.
  """
  dump_log_and_print ('depth', 'thread main created.')
  load()
  dump_log_and_print ('depth', 'thread main loaded.')

  while not pop_flag('exit'):
    if pop_flag('reload'):
      load()
      dump_log_and_print ('depth', 'thread main reloaded.')

    for exg in exgList:
      name, prd, lst, _ = exgList[exg]
      if time.time() - lst > prd and not taskQue.has(exg):
        #dump_log_and_print('depth', 'push %s on %s' %(exg, time.time()))
        taskQue.push(exg)

    time.sleep(0.005)

  wait_all()
  dump_log_and_print ('depth', 'thread main terminated.')

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

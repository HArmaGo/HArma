#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import os, sys, threading, time, traceback

from util import dump, flag, pid, que, sig, wdir

def load_task(name):
  """
  >>> exg = load_task('task.depth.okcoin')
  """
  if name in sys.modules:
    del sys.modules[name]
  module = __import__(name, globals(), locals(), ['*'], 0)
  return module

def wait_all():
  """
  >>> wait_all() #doctest: +ELLIPSIS
  [...] ... threads worker terminated.
  """
  flag.set_flag('exit_worker')
  if len(thPool) > 0:
    for th in thPool:
      th.join()
    dump.dump_log_and_print ('zealot', '%d threads worker terminated.' %len(thPool))
  flag.pop_flag('exit_worker')

def __test1(f):
  """
  >>> __test1('exit')
  >>> flag.pop_flag('exit')
  True
  """
  time.sleep(0.500)
  flag.set_flag(f)

taskList = []
thPool = {}
taskQue = que.que(1)

def load():
  """
  >>> load() #doctest: +ELLIPSIS
  [...] ... threads worker created.
  """
  global taskList, thPool, taskQue, mainSleep, workerSleep
  cfgFile = '$HArmaRoot/bin/cfg'

  mainSleep = float(wdir.load_cfg_field(cfgFile, 'mainSleep'))
  workerSleep = float(wdir.load_cfg_field(cfgFile, 'workerSleep'))

  # wait all threads
  wait_all()

  # setup exchanges
  taskList = {}
  tasks = wdir.load_cfg_field(cfgFile, 'tasks')
  for task in tasks:
    name, prd, enable = task['name'], float(task['period']), task['enable']
    if enable:
      taskList[name] = [ load_task(name), prd, 0 ]

  # clear queue
  thSize = wdir.load_cfg_field(cfgFile, 'maxThNum')
  taskQue = que.que(thSize)

  # start all threads
  thPool = [ threading.Thread(target=worker) for i in range(thSize) ]
  for th in thPool:
    th.start()
  dump.dump_log_and_print ('zealot', '%d threads worker created.' %len(thPool))

def worker():
  """
  >>> threading.Thread(target=__test1, args=('exit_worker',)).start()
  >>> worker()
  """
  while not flag.get_flag('exit_worker'):
    try:
      task = taskQue.pop()
      if task:
        assert task in taskList
        module, prd, lst = taskList[task]
        taskList[task][2] = time.time()

        module.task()
      else:
        time.sleep(workerSleep)
    except:
      dump.dump_exception('zealot')

def main():
  """
  >>> threading.Thread(target=__test1, args=('exit',)).start()
  >>> main() #doctest: +ELLIPSIS
  [...] thread main created.
  [...] ... threads worker created.
  [...] thread main loaded.
  [...] ... threads worker terminated.
  [...] thread main terminated.
  """
  dump.dump_log_and_print ('zealot', 'thread main created.')
  load()
  dump.dump_log_and_print ('zealot', 'thread main loaded.')

  while not flag.pop_flag('exit'):
    try:
      if flag.pop_flag('reload'):
        load()
        dump.dump_log_and_print ('zealot', 'thread main reloaded.')

      for task in taskList:
        module, prd, lst = taskList[task]
        if time.time() - lst > prd and not taskQue.has(task):
          taskQue.push(task)

      time.sleep(mainSleep)
    except:
      dump.dump_exception('zealot')

  wait_all()
  dump.dump_log_and_print ('zealot', 'thread main terminated.')

if __name__ == '__main__':
  if len(sys.argv) != 2 or sys.argv[1] != 'forever':
    import doctest
    print (doctest.testmod())
    print ('Usage: %s forever' % sys.argv[0])
    exit()

  try:
    pid.create_pid_file('zealot')
    sig.reg_exit_signal()
    sig.reg_reload_signal()
    main()
  except:
    dump.dump_exception('zealot')
  finally:
    pid.remove_pid_file('zealot')

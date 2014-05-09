#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import signal

import flag

sig_flag = {}

def __handler(signum, frame):
  """
  >>> flag.get_flag('exit')
  False
  >>> __handler(signal.SIGINT, None)
  >>> flag.get_flag('exit')
  True
  """
  if signum in sig_flag:
    flag.set_flag(sig_flag[signum])

def __bind_signal(signum, flag):
  """
  >>> __bind_signal(signal.SIGINT, 'exit')
  >>> sig_flag[signal.SIGINT]
  'exit'
  """
  global sig_flag
  sig_flag[signum] = flag
  signal.signal(signum, __handler)

def reg_reload_signal():
  """
  >>> reg_reload_signal()
  >>> sig_flag[signal.SIGWINCH]
  'reload'
  """
  # SIGWINCH = 28
  __bind_signal(signal.SIGWINCH, 'reload')

def reg_exit_signal():
  """
  >>> reg_exit_signal()
  >>> sig_flag[signal.SIGINT]
  'exit'
  """
  # SIGINT = 2 (Ctrl+C)
  __bind_signal(signal.SIGINT, 'exit')
  # SIGTERM = 15 (Ctrl+C)
  __bind_signal(signal.SIGTERM, 'exit')

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

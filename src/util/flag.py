#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

FLAG = {}

def set_flag(flag = 'exit'):
  """
  >>> set_flag('exit')
  >>> pop_flag('exit')
  True
  """
  FLAG[flag] = True

def __unset_flag(flag):
  """
  >>> set_flag('exit')
  >>> __unset_flag('exit')
  >>> pop_flag('exit')
  False
  """
  FLAG[flag] = False

def pop_flag(flag):
  """
  >>> set_flag('exit')
  >>> pop_flag('exit')
  True
  >>> pop_flag('exit')
  False
  """
  if flag in FLAG and FLAG[flag]:
    __unset_flag(flag)
    return True
  return False

def get_flag(flag = 'exit'):
  """
  >>> set_flag('exit')
  >>> get_flag('exit')
  True
  >>> get_flag('exit')
  True
  """
  return flag in FLAG and FLAG[flag]

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

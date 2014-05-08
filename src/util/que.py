#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

class que():

  def __init__(self, size):
    """
    >>> not ins
    False
    """
    self.queueSize = size
    self.taskQueue = []
    self.queueLock = threading.Lock()

  def clear(self):
    """
    >>> ins.clear()
    >>> len(ins.taskQueue)
    0
    """
    self.queueLock.acquire()
    taskQueue = []
    self.queueLock.release()

  def pop(self):
    """
    >>> ins.push('a')
    'a'
    >>> ins.push('b')
    'b'
    >>> ins.push('c')
    >>> x = ins.pop()
    >>> x = ins.pop()
    """
    self.queueLock.acquire()
    try:
      if len(self.taskQueue) > 0:
        task = self.taskQueue[0]
        del self.taskQueue[0]
        return task
    finally:
      self.queueLock.release()
    
  def push(self, task):
    """
    >>> x = ins.push('a')
    >>> x = ins.push('b')
    >>> ins.pop()
    'a'
    >>> ins.pop()
    'b'
    >>> ins.pop()
    """
    self.queueLock.acquire()
    try:
      if len(self.taskQueue) < self.queueSize: 
        self.taskQueue.append(task)
        return task
    finally:
      self.queueLock.release()

  def has(self, task):
    """
    >>> ins.has('a')
    False
    >>> x = ins.push('a')
    >>> ins.has('a')
    True
    >>> x = ins.pop()
    """
    self.queueLock.acquire()
    try:
      return task in self.taskQueue
    finally:
      self.queueLock.release()

if __name__ == '__main__':
  import doctest
  print (doctest.testmod(extraglobs={'ins': que(2)}))

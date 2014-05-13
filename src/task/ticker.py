#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

import glob, json, os, shutil

from util import fmt, dump

orig = os.path.expandvars('$HArmaRoot/log/depth')
dest = os.path.expandvars('$HArmaRoot/log/ticker')

def read(fname):
  """
  >>> path1 = os.path.expandvars("$HArmaRoot/log/depth/btc-cny/okcoin/%s.log" %fmt.get_date())
  >>> x = read(path1)
  >>> len(x) > 0
  True
  """
  records = {}
  with open(fname, 'r', encoding = 'utf-8') as myFile:
    lines = myFile.readlines()

    last = 0
    for l in lines:
      h, m, j = l[1:3], l[4:6], l[11:]
      try:
        tag = '[%s:%s0:00]' %(h, m[0])
        if tag not in records:
          jason = json.loads(j)
          records[tag] = json.dumps([ jason[0][0][0], jason[1][0][0] ])
      except:
        dump.dump_exception('ticker')
    return records

def convert(src, dst):
  """
  >>> path1 = os.path.expandvars("$HArmaRoot/log/depth/btc-cny/okcoin/%s.log" %fmt.get_date())
  >>> path2 = os.path.expandvars("$HArmaRoot/trash/x")
  >>> if os.path.isfile(path2): os.remove(path2)
  >>> convert(path1, path2)
  >>> os.path.isfile(path2)
  True
  >>> if os.path.isfile(path2): os.remove(path2)
  """
  with open(dst, 'w', encoding = 'utf-8') as myFile:
    records = read(src)
    for tag in sorted(records.keys()):
      myFile.write('%s %s\n' %(tag, records[tag]))

def task():
  """
  >>> path1 = os.path.expandvars("$HArmaRoot/log/depth/btc-cny/okcoin/%s.log" %fmt.get_date())
  >>> path2 = os.path.expandvars("$HArmaRoot/log/depth/xxx-yyy/okcoin/%s.log" %fmt.get_date())
  >>> path3 = os.path.expandvars("$HArmaRoot/log/ticker/xxx-yyy/okcoin/%s.log" %fmt.get_date())
  >>> path4 = os.path.expandvars("$HArmaRoot/log/depth/xxx-yyy")
  >>> path5 = os.path.expandvars("$HArmaRoot/log/ticker/xxx-yyy")
  >>> path6 = os.path.expandvars("$HArmaRoot/log/depth/xxx-yyy/okcoin")
  >>> if os.path.exists(path4): shutil.rmtree(path4)
  >>> if os.path.exists(path5): shutil.rmtree(path5)
  >>> os.makedirs(path6)
  >>> x = shutil.copyfile(path1, path2)
  >>> task()
  >>> os.path.exists(path3)
  True
  >>> shutil.rmtree(path4)
  >>> shutil.rmtree(path5)
  """
  if os.path.isdir(orig):
    for fP in [ fP for fP in glob.glob(os.path.join(orig, '*-*/*')) if \
                os.path.isdir(fP) ]:
      if not os.path.exists(dest + fP[len(orig):]):
        os.makedirs(dest + fP[len(orig):])
    for fP in [ fP for fP in glob.glob(os.path.join(orig, '*-*/*/%s.log' %fmt.get_date())) if \
                os.path.isfile(fP) ]:
      convert(fP, dest + fP[len(orig):])

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

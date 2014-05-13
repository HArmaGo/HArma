#!/usr/bin/env python3.4
# -*- coding: utf-8 -*-

def is_valid_price(price): return price > 0
def is_valid_amount(amount): return amount > 0.00001 

def is_valid_order(order):
  """
  >>> is_valid_order((5000,1))
  True
  >>> is_valid_order((5000,0))
  False
  """
  return len(order)==2 and \
         is_valid_price(order[0]) and is_valid_amount(order[1])

def is_valid_bid(bid): return is_valid_order(bid)
def is_valid_ask(ask): return is_valid_order(ask)

def is_valid_orderbook(book):
  """
  >>> is_valid_orderbook(())
  False
  >>> is_valid_orderbook(((5000,1),(4900,0.2)))
  True
  """
  return len(book)>0 and all(is_valid_order(order) for order in book)

def is_valid_bidbook(book):
  """
  >>> is_valid_bidbook(((5000,1),(4900,1)))
  True
  >>> is_valid_bidbook(((5000,1),(5100,1)))
  False
  """
  return is_valid_orderbook(book) and \
         all(book[i][0]>=book[i+1][0] for i in range(len(book)-1))

def is_valid_askbook(book):
  """
  >>> is_valid_askbook(((5000,1),(4900,1)))
  False
  >>> is_valid_askbook(((5000,1),(5100,1)))
  True
  """
  return is_valid_orderbook(book) and \
         all(book[i][0]<=book[i+1][0] for i in range(len(book)-1))

def is_valid_depth(book):
  """
  >>> is_valid_depth(())
  False
  >>> is_valid_depth((((5000,1),),((5100,1),)))
  True
  """
  if not book: return False
  return len(book)==2 and \
         is_valid_bidbook(book[0]) and is_valid_askbook(book[1]) and \
	 book[0][0][0] < book[1][0][0]

def is_valid_bidaskbook(book): return is_valid_depth(book)
def is_valid_exchangename(name): return len(name)>0
def is_valid_goodsname(name): return len(name)>0

def is_valid_goodsratename(name):
  """
  >>> is_valid_goodsratename('')
  False
  >>> is_valid_goodsratename('cny-')
  False
  >>> is_valid_goodsratename('cny-btc')
  True
  """
  return name.count('-')==1 and len(name.split('-'))==2 and \
         all([is_valid_goodsname(n) for n in name.split('-')])

def is_valid_goodsrate(rate):
  """
  >>> is_valid_goodsrate(('okcoin', 'btc-cny', (((5000,1),),((5100,1),))))
  True
  """
  return len(rate)==3 and is_valid_exchangename(rate[0]) and \
         is_valid_goodsratename(rate[1]) and is_valid_depth(rate[2])

def is_valid_goodsrates(rates):
  """
  >>> is_valid_goodsrates([('okcoin', 'btc-cny', (((5000,1),),((5100,1),)))])
  True
  """
  return all([is_valid_goodsrate(rate) for rate in rates])

if __name__ == '__main__':
  import doctest
  print (doctest.testmod())

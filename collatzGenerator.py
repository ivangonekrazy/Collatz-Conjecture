#
# Collatz sequence generator.
# (http://en.wikipedia.org/wiki/Collatz_conjecture)
#
# Python generator function version.
#
# Copyright (c)2011, Ivan Tam. ivan@hipnik.net
#

def collatzGen(n):
  if n == 1: yield 1  # base case
  else: yield n

  while n > 1:
    if   n % 2 == 1: n = n * 3 + 1
    elif n % 2 == 0: n = n / 2
    yield n

if __name__ == '__main__':
  print [ x for x in collatzGen(1024)]
  print [ x for x in collatzGen(50)]
  print [ x for x in collatzGen(1)]

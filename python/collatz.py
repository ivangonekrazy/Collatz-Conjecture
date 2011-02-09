#
# Collatz sequence generator.
# (http://en.wikipedia.org/wiki/Collatz_conjecture)
#
# Recursive (with accumulator) Python version.
#
# Copyright (c)2011, Ivan Tam. ivan@hipnik.net
#

def collatz(n, acc=None):
  # if the accumulator is not set, give it a head
  if acc is None: acc = [n]

  # base case
  if n == 1: return [1]

  if n % 2 == 1:     # odd case
    next = n * 3 + 1
  elif n % 2 == 0:   # even case
    next = n / 2

  acc.append( next )
  collatz( next, acc )
  return acc

if __name__ == '__main__':
  print collatz(1024)
  print collatz(50)
  print collatz(1)

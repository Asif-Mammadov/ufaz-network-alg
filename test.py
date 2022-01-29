import math
def func(n):
  print((n+1) ** (1/n) - n**(1/n))


for i in range(1, 1000):
  func(i)
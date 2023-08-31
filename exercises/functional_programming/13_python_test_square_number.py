n=25
def is_square(n):
  root = int(n ** 0.5)
  if root * root == n: 
    return True
  else: 
    return False

def is_square(n):    
    return n >= 0 and (n**0.5) % 1 == 0

import math
def is_square(n):
    return n > -1 and math.sqrt(n) % 1 == 0
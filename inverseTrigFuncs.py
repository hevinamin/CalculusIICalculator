from integral import integrate
from pi import pi

def arcsin(val):
  if abs(val) > 1:
    return ("undefined")
  return integrate('1/(1-x**2)**0.5', 0, val)

def arctan(val):
  if val == 0: 
    return 0
  if val > 1:
    return pi() / 2 - integrate('1/(1+x**2)', 0, 1/val)
  return integrate('1/(1+x**2)', 0, val)

def arcsec(val):
  if abs(val) < 1:
    return 'undefined'
  return arccos(1/val)

def arccos(val):
  if abs(val) > 1:
    return 'undefined'
  return -(arcsin(val) - pi()/2)


def arccot(val):
  return arctan(1/val)

def arccsc(val):
  return arcsin(1/val)
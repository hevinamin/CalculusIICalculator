from derivative import derivative
from mathParser import evalFunction


def linear(a, b):
  return lambda x: a * x + b


def quadratic(a, b, c):
  return lambda x: a * x**2 + b * x + c


def cubic(a, b, c, d):
  return lambda x: a * x**3 + b * x**2 + c * x + d



def findZeros(function, initialVal, leftBound, rightBound):
  next = initialVal
  if initialVal<leftBound or initialVal>rightBound:
    return "undefined"
  while abs(evalFunction(function, next)) > 0.0001:
    if next > rightBound or next < leftBound:
      return "undefined"
    next = next - (evalFunction(function, next) / derivative(function, next))
  return next
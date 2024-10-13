from basicOperations import factorial
from pi import pi

def sine(val):

  val %= (2 * pi())

  answer = val
  sign = -1
  precision = 100
  n = 3

  while n < precision:
    answer += val ** n / factorial(n) * sign
    n += 2
    sign *= -1
  return answer

def cosine(val):
  answer = 1
  sign = -1
  precision = 100
  n = 2

  val %= (2 * pi())

  while n < precision:
    answer += val ** n / factorial(n) * sign
    n += 2
    sign *= -1
  return answer

def tan(val):
  return sine(val) / cosine(val)

def cosecant(val):
  return 1 / sine(val)

def secant(val):
  return 1 / cosine(val)

def cotangent(val):
  return 1 / tan(val)
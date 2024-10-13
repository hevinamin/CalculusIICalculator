def factorial(val):
  ans = 1
  for i in range(1, val+1):
    ans *= i
  return ans

def sqrt(val):
  return val ** 0.5

def nroot(base, n):
  return base ** (1/n)
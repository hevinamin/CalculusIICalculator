from basicOperations import factorial
from integral import integrate

def e_x (val):
  answer = 1
  precision = 100
  n = 1

  while n < precision:
    answer += val ** n / factorial(n)
    n +=1
  return answer

def ln(val):
  if val <= 0: 
    return 'undefined'

  answer = 0
  if val > 100:
    answer += ln(100) + ln(val/100)
    val /= 100
    return answer
  return integrate('1/x', 1, val)

def log(val, base):
  return ln(val) / ln(base)
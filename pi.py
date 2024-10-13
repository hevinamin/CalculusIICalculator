def arctan_taylor(val):
  answer = val
  sign = -1
  precision = 155
  n = 3

  while n < precision:
    answer += val ** n / (n) * sign
    n += 2
    sign *= -1
  return answer

def pi():
  return 4 * (4 * arctan_taylor(1/5) - arctan_taylor(1/239)) # machin's formula
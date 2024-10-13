from main import factorial, power

num = float(input("Tan of? \n"))

def sine(val):

  while val > 2 * 3.14:
    val -= 2 * 3.14159265358979323
  while val < -2 * 3.14:
    val += 2 * 3.14159265358979323

  answer = val
  sign = -1
  precision = 155
  n = 3

  while n < precision:
    answer += power(val, n) / factorial(n) * sign
    n += 2
    sign *= -1
  return answer

def cosine(val):
  answer = 1
  sign = -1
  precision = 155
  n = 2

  while val > 2 * 3.14:
    val -= 2 * 3.14159265358979323
  while val < -2 * 3.14:
    val += 2 * 3.14159265358979323

  while n < precision:
    answer += power(val, n) / factorial(n) * sign
    n += 2
    sign *= -1
  return answer


def tan(val):
  answer = sine(val) / cosine(val)
  return answer

print("Tan","(",num,") =",+tan(num))

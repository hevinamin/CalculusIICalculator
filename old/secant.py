from main import power, factorial

num = float(input("Secant of? \n"))

def cosine(val):
  answer = 1
  sign = -1
  precision = 100
  n = 2

  while n < precision:
    answer += power(val, n) / factorial(n) * sign
    n += 2
    sign *= -1
  return answer


def secant(val):
  answer = 1 / cosine(val)
  return answer

print("Secant of", num, "=", secant(num))

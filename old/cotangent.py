from main import power, factorial

num = float(input("Cotangent of? \n"))

def sine(val):
  answer = val
  sign = -1
  precision = 100
  n = 3
  if val < 0:
    while val < 0:
      val += 2 * 3.14
      # generate pi later, currently just a placeholder
  while n < precision:
    answer += power(val, n) / factorial(n) * sign
    n += 2
    sign *= -1
  return answer

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


def cotangent(val):
  if sine (val) == 0:
    return "undefined"
  else:
    return cosine(val) / sine(val)
print("Cotangent of", num, "=", cotangent(num))

from main import power, factorial

value = float(input("Cosecant of? \n"))

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

def cosecant(val):
  if sine(val) == 0:
    return "undefined"
  else:
    return 1/sine(val)

print("Cosecant of", value, "=", cosecant(value))
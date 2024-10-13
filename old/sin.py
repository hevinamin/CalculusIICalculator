from main import factorial

value = float(input("Sine of? \n"))


def sine(val):

  val %= (2 * 3.141592653589)

  answer = val
  sign = -1
  precision = 155
  n = 3

  while n < precision:
    answer += val ** n / factorial(n) * sign
    n += 2
    sign *= -1
  return answer


print("Sine","(",value,") =",+sine(value))

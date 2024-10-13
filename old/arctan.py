value = float(input("Arctan of? \n"))


def arctan(val):


  answer = val
  sign = -1
  precision = 155
  n = 3

  while n < precision:
    answer += val ** n / (n) * sign
    n += 2
    sign *= -1
  return answer


print("Arctan","(",value,") =",arctan(value))

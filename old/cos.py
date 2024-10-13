from main import factorial

value = float(input("Cosine of? \n"))

def cosine(val):
  answer = 1
  sign = -1
  precision = 155
  n = 2

  val %= (2 * 3.141592653589)
  
  while n < precision:
    answer += val ** n / factorial(n) * sign
    n += 2
    sign *= -1
  return answer

print("Cosine","(",value,") =",+cosine(value))
  

from main import factorial

value = float(input("e^x for x=? \n"))
def e_x (value):
  answer = 1
  precision = 100
  n = 1

  while n < precision:
    answer += value ** n / factorial(n)
    n +=1
  return answer

print ("e^",value,"=", e_x(value))




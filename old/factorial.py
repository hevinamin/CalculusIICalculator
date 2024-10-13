val = int(input("Factorial of? \n"))
ans = 1

def factorial(val):
  global ans
  for i in range(1, val+1):
    ans *= i
  return ans

print(val,"! =",factorial(val))
def ln(x):
  if x <= 0:
    return "undefined"
  value = float(x) - 1
  returnValue = 0
  sign = -1
  for i in range(1,100):
    returnValue += pow(value, i) * sign / i
    sign *= -1
  return returnValue

x = float(input("Ln of? \n"))
print("ln(",x,") =", ln(x))
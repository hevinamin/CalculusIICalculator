from mathParser import evalFunction
# function = input("Derivative of? \n")
# x = float(input("At what x value? \n"))

def derivative(function, val):
  h = 0.0000001
  return (evalFunction(function, val+h) - evalFunction(function, val)) / h
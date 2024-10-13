from derivative import derivative
from mathParser import evalDerivative


def eulers_method_derivative(fderivative, x0, y0, xf, step):
  x = x0
  y = y0
  solution = [(x,y)]
  while abs(x - xf) > 0.000001:
    y = y + step * evalDerivative(fderivative, x, y)
    x = x + step
    solution.append((x,y))
  return solution
# solution = eulers_method(lambda x, y: x + y, 0, 0, 1, 0.5)
# print(solution) 

def eulers_method_function(function, y0, x0, xf, step):
  x = x0
  y = y0
  solution = [(x,y)]
  while abs(x - xf) > 0.000001:
    y = y + step * derivative(function, x)
    x = x + step
    solution.append((x,y))
  return solution
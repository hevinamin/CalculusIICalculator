
def trapezoidRiemannSum(function, leftBound, rightBound, n):
  deltaX = (rightBound - leftBound) / n
  answer = 0
  step = leftBound
  for i in range(n):
    answer += (eval(function.replace('x', '(' + str(step) + ')')) + eval(function.replace('x', '(' + str(step + deltaX) + ')'))) * deltaX / 2
    step += deltaX
  return answer


print(trapezoidRiemannSum('3*x+5',0,5,4))
print(trapezoidRiemannSum('x**2', 0, 2, 10))


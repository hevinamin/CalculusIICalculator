inputValue = input("input function\n")

def MidpointRiemannSum(function):
  leftBound = float(input('left bound\n'))
  rightBound = float(input('right bound\n'))
  n = int(input('how many rectangles\n'))

  deltaX = (rightBound - leftBound) / n
  answer = 0
  step = (2*leftBound + deltaX) / 2
  for i in range(n):
    answer += eval(function.replace('x', '(' + str(step) + ')')) * deltaX
    step += deltaX
  return answer

print(MidpointRiemannSum(inputValue))

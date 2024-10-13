inputValue = input("input function\n")

def RightRiemannSum(function):
  leftBound = float(input('left bound\n'))
  rightBound = float(input('right bound\n'))
  n = int(input('how many rectangles\n'))

  deltaX = (rightBound - leftBound) / n
  answer = 0
  step = leftBound + deltaX
  for i in range(n):
    answer += eval(function.replace('x', '(' + str(step) + ')')) * deltaX
    step += deltaX
  return answer

print(RightRiemannSum(inputValue))
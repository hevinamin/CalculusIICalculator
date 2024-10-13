inputValue = input("input function\n")
leftBound = float(input('left bound\n'))
rightBound = float(input('right bound\n'))
n = int(input('how many rectangles\n'))

def leftRiemannSum(function, leftBound, rightBound, n):
  deltaX = (rightBound - leftBound) / n
  answer = 0
  step = leftBound
  for i in range(n):
    answer += eval(function.replace('x', '(' + str(step) + ')')) * deltaX
    step += deltaX
  return answer

print(leftRiemannSum(inputValue, leftBound, rightBound, n))

from mathParser import evalFunction

def leftRiemannSum(function, leftBound, rightBound, n):
  deltaX = (rightBound - leftBound) / n
  answer = 0
  step = leftBound
  for i in range(n):
    answer += evalFunction(function, step) * deltaX
    step += deltaX
  return answer

def rightRiemannSum(function, leftBound, rightBound, n):
  deltaX = (rightBound - leftBound) / n
  answer = 0
  step = leftBound + deltaX
  for i in range(n):
    answer += evalFunction(function, step) * deltaX
    step += deltaX
  return answer

def midpointRiemannSum(function, leftBound, rightBound, n):
  deltaX = (rightBound - leftBound) / n
  answer = 0
  step = (2*leftBound + deltaX) / 2
  for i in range(n):
    answer += evalFunction(function, step) * deltaX
    step += deltaX
  return answer

def trapezoidRiemannSum(function, leftBound, rightBound, n):
  deltaX = (rightBound - leftBound) / n
  answer = 0
  step = leftBound
  for i in range(n):
    answer += (evalFunction(function, step) + evalFunction(function, step)) * deltaX / 2
    step += deltaX
  return answer
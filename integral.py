from riemannSums import midpointRiemannSum

def integrate(function, leftBound, rightBound):
  return midpointRiemannSum(function, leftBound, rightBound, 300)
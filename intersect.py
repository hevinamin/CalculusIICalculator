from Zeros import findZeros

def findIntersect(function0, function1, guess, leftBound, rightBound):
  return findZeros('(' + str(function0) + ')' +  '-' + '(' + str(function1) + ')', guess, leftBound, rightBound)
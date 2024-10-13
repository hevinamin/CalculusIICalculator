from basicOperations import sqrt
from derivative import derivative
from eulers import eulers_method_derivative, eulers_method_function
from riemannSums import leftRiemannSum, rightRiemannSum, midpointRiemannSum, trapezoidRiemannSum
from integral import integrate
from mathParser import parseMath
from Zeros import findZeros
from intersect import findIntersect

# to-do list:
#   - try to break everything

print('\nNOTE: if entering a function, put parentheses around the argument (i.e. sin(3) not sin3)')
print('      use asterisks for all multiplication (parenthese don\'t work)')
print('      logs must be in the form log(value,base)')
print('      roots must be in the form of exponents')
print('      e\'s (Euler\'s numbers) must be uppercase\n')

choice = input("what function would you like?\nchoices: sci, calc, graph\n")

if choice == "sci":
  input = input('enter your equation\n')
  print(parseMath(input))

elif choice == 'calc':
  choice = input('what button?\nchoices: derivative, rms, integral, euler\n')
  function = input('input function\n')

  if choice == 'rms':
    leftBound = parseMath(input('left bound?\n'))
    rightBound = parseMath(input('right bound?\n'))
    n = int(input('number of rectangles?\n'))

    choice = input('which type?\n')

    if choice == 'left':
      print(leftRiemannSum(function, leftBound, rightBound, n))
    if choice == 'right':
      print(rightRiemannSum(function, leftBound, rightBound, n))
    if choice == 'midpoint':
      print(midpointRiemannSum(function, leftBound, rightBound, n))
    if choice == 'trapezoid':
      print(trapezoidRiemannSum(function, leftBound, rightBound, n))
  

  if choice == "integral":
    leftBound = parseMath(input('left bound?\n'))
    rightBound = parseMath(input('right bound?\n'))
    print(integrate(function, leftBound, rightBound))

  if choice == "derivative":
    val = parseMath(input('at what value?\n'))
    print(derivative(function, val))

  if choice == "euler":
    leftBound = parseMath(input('initial x?\n'))
    y0 = parseMath(input('initial y?\n'))
    rightBound = parseMath(input('final x?\n'))
    stepSize = float(input('step size?\n'))
    choice = input('is the function the derivative?\n')
    if choice == 'yes':
      print(eulers_method_derivative(function, leftBound, y0, rightBound, stepSize))
    if choice == 'no':
      print(eulers_method_function(function, y0, leftBound, rightBound, stepSize))

elif choice == 'graph':
  choice = input('what button?\nchoice: zeros, intersect\n')
  leftBound = parseMath(input('left bound?\n'))
  rightBound = parseMath(input('right bound?\n'))
  guess = parseMath(input('guess?\n'))
  
  if choice == 'zeros':
    function = input('input function\n')
    print(findZeros(function, guess, leftBound, rightBound))
  
  if choice == 'intersect':
    function0 = input('input function0\n')
    function1 = input('input function1\n')
    print(findIntersect(function0, function1, guess, leftBound, rightBound))

else:
  print('button not found')

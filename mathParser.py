# to do:
#   - all done! (hopefully)

def parseMath(expression):
  from trigFuncs import sine, cosine, tan, cosecant, secant, cotangent
  from logarithmicFuncs import e_x, ln, log
  from pi import pi
  from inverseTrigFuncs import arcsin, arccos, arcsec, arccsc, arctan, arccot
  
  functions = {'arcsin' : arcsin,
               'arccos' : arccos,
               'arcsec' : arcsec,
               'arccsc' : arccsc,
               'arctan' : arctan,
               'arccot' : arccot,
                  'sin' : sine, 
                  'cos' : cosine, 
                  'tan' : tan,
                  'csc' : cosecant,
                  'sec' : secant,
                  'cot' : cotangent,
                  'log' : log,
                  'ln'  : ln
              }
  
  keywords = {'E' : e_x(1),
              'pi' : pi()
              }

  for i in keywords:
    while i in expression:
      pos = expression.find(i)
      keyIndex = list(keywords.keys()).index(i)
      expression = expression.replace(
        expression[pos : pos + keyIndex + 1], str(keywords[i])
      )
    
  for i in functions:
    pos = 0
    cutUp = expression[pos: ]

    while i in cutUp:
      leftParen = expression.index(i) + len(i)
      cutUp = expression[leftParen: ]
      rightParen = leftParen + (findRightParen(cutUp) - cutUp.find('('))

      if i == 'log':
        curAnswer = functions[i](
          float(
            eval(expression[leftParen + 1 : rightParen].split(',')[0])
          ),
          float(
            eval(expression[leftParen + 1 : rightParen].split(',')[1])
          )
        )
        
      else:
        curAnswer = functions[i](
          float(
            eval(expression[leftParen + 1 : rightParen])
          )
        )

      expression = expression.replace(
        expression[leftParen-len(i) : rightParen + 1], '(' + str(curAnswer) + ')'
      )

      # print(expression)
  # print("done")
  return eval(expression)

def findRightParen(input):
  rightCounter = 0
  leftCounter = 1
  pos = 0
  for i in input[1:]:
    if rightCounter == leftCounter:
      break
    if i == "(":
      leftCounter += 1
    if i == ")":
      rightCounter += 1
      rightParen = pos
    pos += 1

  return rightParen + 1

# print(findRightParen('(3 + (4+5))'))
# #                     0123456789012

def evalFunction(function, value):
  return parseMath(function.replace('x', '(' + str(value) + ')'))

def evalDerivative(function, xVal, yVal):
  return parseMath(function.replace('x', '(' + str(xVal) + ')').replace('y', '(' + str(yVal) + ')'))
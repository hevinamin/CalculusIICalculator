def pi():
  precision = 7500000
  n = 1
  sign= 1
  answer= 0
  while n < precision:  
    answer += sign / n
    n += 2
    sign *= -1
  return answer * 4

num=float(input("Pi divided by? \n"))
print("Pi divided by",num,"=",pi()/num)
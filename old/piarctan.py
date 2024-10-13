def piarctan(val):

  answer = val
  sign = -1
  precision = 155
  n = 3

  while n < precision:
    answer += val ** n / (n) * sign
    n += 2
    sign *= -1
  return answer


# print("Pi=",4*piarctan(1))
print(4 * (4 * piarctan(1/5) - piarctan(1/239))) # Machin formula

pi = 4 * (4 * piarctan(1/5) - piarctan(1/239))
print(f'{pi:.14f}') # accurate to 14 digits?

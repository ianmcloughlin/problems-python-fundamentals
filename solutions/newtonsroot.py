# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

def newtonsroot(x):
  # Set the initial guess to anything. Try half of x.
  z = x / 2.0
  # Set the next guess using the formula.
  n = z - ((z**2 - x)/(2 * z))
  # Keep looping until the difference between the current guess
  # and the next guess is less than 0.000001.
  while abs(z - n) >= 0.0000001:
    z = n
    n = z - ((z**2 - x)/(2 * z))
  return n

# Tests from question.
print(newtonsroot(100))
print(newtonsroot(144))
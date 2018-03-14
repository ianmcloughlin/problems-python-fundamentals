# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

# We need to calculate the factorial on a number.
def fac(n):
  # ans will be the factorial by the end.
  ans = 1
  # Loop through the numbers i from 1 to n.
  for i in range(1, n+1):
    # Multiply ans by i, changing ans to that.
    ans *= i
  # Return the factorial.
  return ans


def etondecs(n):
  # See https://en.wikipedia.org/wiki/E for method
  # Set e to 1.
  e = 1.0
  # Set i to 0.
  i = 1
  # Calculate the next approximation of e.
  ap = e + (1.0 / fac(i))
  # Calculate the minimum change in guesses.
  d = 1.0 / 10**(n+1)
  # Keep looping until the difference between the current guess
  # and the next guess is less than 0.000001.
  while abs(e - ap) >= d:
    # Increase i by 1.
    i = i + 1
    # Set pi to the next approximation.
    e = ap
    # Calculate the next approximation.
    ap = e + (1.0 / fac(i))
  # Round e to n decimal places and return.
  return round(e, n)

# Tests from question.
print(etondecs(2))
print(etondecs(6))
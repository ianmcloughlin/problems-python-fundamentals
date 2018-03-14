# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

def pitondecs(n):
  # See https://www.wikihow.com/Calculate-Pi for method
  # Set pi to 0.
  pi = 0.0
  # Set i to 0.
  i = 0
  # Calculate the next approximation of pi.
  ap = pi + (8.0 / (((4.0 * i) + 1) * ((4.0 * i) + 3.0)))
  # Calculate the minimum change in guesses.
  d = 1.0 / 10**(n+1)
  # Keep looping until the difference between the current guess
  # and the next guess is less than 0.000001.
  # Warning: this doesn't converge quick enough.
  while abs(pi - ap) >= d:
    # Increase i by 1.
    i = i + 1
    # Set pi to the next approximation.
    pi = ap
    # Calculate the next approximation.
    ap = pi + (8.0 / (((4.0 * i) + 1) * ((4.0 * i) + 3.0)))
  # Round pi to n decimal places and return.
  return round(pi, n)

# Tests from question.
print(pitondecs(2))
print(pitondecs(6))
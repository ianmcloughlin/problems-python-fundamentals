# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

def compoundinterest(p, r, n):
  # Loop over the periods.
  for i in range(n):
    # Increase the principal.
    p = p + (p * (0.01 * r))
  # Return the final principal, rounded to nearest cent.
  return round(p, 2)

# Tests from question.
print(compoundinterest(1000, 3, 5))
print(compoundinterest(1000, 7, 10))
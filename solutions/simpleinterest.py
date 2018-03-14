# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

def simpleinterest(p, r, n):
  # Calculate the interest for one period.
  i = p * (0.01 * r)
  # Calculate the interest for all periods.
  t = i * n
  # Return the total interest plus principal, rounded.
  return round(p + t, 2)

# Tests from question.
print(simpleinterest(1000, 3, 5))
print(simpleinterest(1000, 7, 10))
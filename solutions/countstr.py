# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

def countstr(s):
  # The dictionary that will contain the answer.
  ans = {}
  # Loop through the string.
  for c in s:
    ans[c] = ans.get(c, 0) + 1
  # Return the dictionary.
  return ans

# Tests from question.
print(countstr('aaacbb'))
print(countstr('Hello, world!'))
# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

def sortlist(l):
  # Loop through the elements of the list.
  for i in range(len(l)):
    # Loop through the remaining elements of the list.
    for j in range(i+1, len(l)):
      # If the i^th element is greater than the j^th.
      if l[i] > l[j]:
        # Swap them.
        l[i], l[j] = l[j], l[i]
  # Return the sorted list.
  return l

# Tests from question.
print(sortlist([3,1,2]))
print(sortlist([10,-9,5,-1,0]))
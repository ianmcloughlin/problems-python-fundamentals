# Ian McLoughlin, 2018-03-14
# https://github.com/ianmcloughlin/problems-python-fundamentals

def caesar(s, n):
  # Turn the string into a list.
  s = list(s)
  # Loop through the string a character at a time.
  for i in range(len(s)):
    # Check if the character is a lowercase letter.
    if ord('a') <= ord(s[i]) <= ord('z'):
      # Calculate its new ord number if so.
      newcord = ord(s[i]) + n
      # If the new character has gone beyond 'z'.
      if newcord > ord('z'):
        # Then wrap it back around to 'a'.
        newcord = newcord - ord('z') + ord('a') - 1
      # Update the character in the string.
      s[i] = chr(newcord)
        # Check if the character is an uppercase letter.
    elif ord('A') <= ord(s[i]) <= ord('Z'):
      # Calculate its new ord number if so.
      newcord = ord(s[i]) + n
      # If the new character has gone beyond 'Z'.
      if newcord > ord('Z'):
        # Then wrap it back around to 'a'.
        newcord = newcord - ord('Z') + ord('A') - 1
      # Update the character in the string.
      s[i] = chr(newcord)
  # Return the updated string.
  return ''.join(s)

# Tests from question.
print(caesar('abcd', 3))
print(caesar('Hello, world!', 2))

# All the lowercase letters.
print(caesar('abcdefghijklmnopqrstuvwxyz', 2))
"""
Assume s is a string of lower case characters.

Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print

Number of times bob occurs is: 2
"""

s = 'azcbobobegghakl'
count = 0

for i in range(len(s)):
  bob = ""
  for x in range(0, 3):
    try:
      bob += str(s[i + x])
    except IndexError:
      bob += ""
  if bob == "bob":
    count += 1

print("Number of times bob occurs is:", count)
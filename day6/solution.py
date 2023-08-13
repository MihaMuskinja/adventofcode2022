#!/usr/bin/python3
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

X = [l.strip() for l in open(os.path.join(__location__, 'input'))]
print(X[0])
datastream_buffer = X[0]


# initialize last_four to be empty
last_four = []

# loop through each character in the datastream buffer
for i, c in enumerate(datastream_buffer):
  # add the character to last_four
  last_four.append(c)

  # if last_four has more than four characters, remove the first character
  if len(last_four) > 14:
    last_four = last_four[1:]

  # check if all characters in last_four are different
  if len(set(last_four)) == 14:
    # if they are, we've found the start-of-packet marker
    print(f"Found start-of-packet marker after {i + 1} characters")
    break
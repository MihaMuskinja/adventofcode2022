#!/usr/bin/python3
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

X = [l.strip() for l in open(os.path.join(__location__, 'input'))]
p1 = 0
p2 = 0

for x in X:
    o, m = x.split()
    o = ord(o) - ord("A")
    m = ord(m) - ord("X")

    p1 += m + 1
    r = (o - m) % 3
    if r == 0:
        p1 += 3
    elif r == 2:
        p1 += 6

    if m == 1:
        p2 += 3 + o + 1
    elif m == 0:
        p2 += (o + 2) % 3  + 1
    else:
        p2 += 6 + (o + 1) % 3 + 1

print(p1)
print(p2)

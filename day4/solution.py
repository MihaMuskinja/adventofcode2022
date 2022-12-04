#!/usr/bin/python3
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

X = [l.strip() for l in open(os.path.join(__location__, 'input'))]
p1 = 0
p2 = 0

for x in X:
    a, b = x.split(",")
    a = a.split("-")
    b = b.split("-")
    if int(a[0]) >= int(b[0]) and int(a[1]) <= int(b[1]):
        p1 += 1
    elif int(b[0]) >= int(a[0]) and int(b[1]) <= int(a[1]):
        p1 += 1

    if (int(a[0]) < int(b[0]) and int(a[1]) < int(b[0])) or (int(b[0]) < int(a[0]) and int(b[1]) < int(a[0])):
        pass
    else:
        p2 += 1
        print(a,b)

print(p1)
print(p2)
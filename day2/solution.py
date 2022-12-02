#!/usr/bin/python3

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input'))

score = 0
for l in f:
    o = l.split()[0]
    me = l.split()[1]
    print(o, me)
    if me == "X":
        score += 1
    if me == "Y":
        score += 2
    if me == "Z":
        score += 3

    if me == "X" and o == "A":
        score += 3
    elif me == "Y" and o == "B":
        score += 3
    elif me == "Z" and o == "C":
        score += 3
    elif me == "X" and o == "C":
        score += 6
    elif me == "Y" and o == "A":
        score += 6
    elif me == "Z" and o == "B":
        score += 6


print(f"solution a) {score}")
f.close()

f = open(os.path.join(__location__, 'input'))

score = 0
for l in f:
    o = l.split()[0]
    me = l.split()[1]
    print(o, me)
    if me == "X":
        if o == "A":
            score += 3
        elif o == "B":
            score += 1
        elif o == "C":
            score += 2
    elif me == "Y":
        score += 3
        if o == "A":
            score += 1
        elif o == "B":
            score += 2
        elif o == "C":
            score += 3
    elif me == "Z":
        score += 6
        if o == "A":
            score += 2
        elif o == "B":
            score += 3
        elif o == "C":
            score += 1


print(f"solution b) {score}")

f.close()

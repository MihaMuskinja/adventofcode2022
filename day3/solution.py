#!/usr/bin/python3
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

X = [l.strip() for l in open(os.path.join(__location__, 'input'))]
p1 = 0
p2 = 0

example = [
"vJrwpWtwJgWrhcsFMMfFFhFp",
"jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL",
"PmmdzqPrVvPwwTWBwg",
"wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn",
"ttgJtRGJQctTZtZT",
"CrZsJsPPZsGzwwsLwLmpwMDw",
]

g1 = ""
g2 = ""
g3 = ""
for x in X:
    if g1 == "":
        g1 = x
    elif g2 == "":
        g2 = x
    elif g3 == "":
        g3 = x
        for c in g1:
            if c in g2 and c in g3:
                if ord(c) <= ord("Z"):
                    p2 += ord(c) - ord("A") + 27
                else:
                    p2 += ord(c) - ord("a") + 1
                g1 = ""
                g2 = ""
                g3 = ""
                break

    a = x[:len(x)//2]
    b = x[len(x)//2:]
    print(a, b)

    for c in a:
        if c in b:
            print(c)
            if ord(c) <= ord("Z"):
                p1 += ord(c) - ord("A") + 27
                print(ord(c) - ord("A") + 27)
            else:
                p1 += ord(c) - ord("a") + 1
                print(ord(c) - ord("a") + 1)
            break

print(p1)
print(p2)
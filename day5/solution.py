#!/usr/bin/python3
import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

X = [l.strip() for l in open(os.path.join(__location__, 'input'))]
p1 = 0
p2 = 0


#             [G] [W]         [Q]    
# [Z]         [Q] [M]     [J] [F]    
# [V]         [V] [S] [F] [N] [R]    
# [T]         [F] [C] [H] [F] [W] [P]
# [B] [L]     [L] [J] [C] [V] [D] [V]
# [J] [V] [F] [N] [T] [T] [C] [Z] [W]
# [G] [R] [Q] [H] [Q] [W] [Z] [G] [B]
# [R] [J] [S] [Z] [R] [S] [D] [L] [J]
#  1   2   3   4   5   6   7   8   9 


stack = [
[x for x in reversed(["Z","V","T","B","J","G","R"])],
[x for x in reversed(["L","V","R","J"])],
[x for x in reversed(["F","Q","S"])],
[x for x in reversed(["G","Q","V","F","L","N","H","Z"])],
[x for x in reversed(["W","M","S","C","J","T","Q","R"])],
[x for x in reversed(["F","H","C","T","W","S"])],
[x for x in reversed(["J","N","F","V","C","Z","D"])],
[x for x in reversed(["Q","F","R","W","D","Z","G","L"])],
[x for x in reversed(["P","V","W","B","J"])],
]

# for x in example.split("\n"):"
for x in X:
    b = [int(x.split()[a]) for a in [1, 3, 5]]
    s1 = stack[b[1]-1]
    s2 = stack[b[2]-1]

    temp = []
    for i in range(b[0]):
        temp += [s1.pop()]
    s2 += [p for p in reversed(temp)]

for s in stack:
    print(s[-1])
print(stack)
print(p2)


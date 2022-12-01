#!/usr/bin/python3

import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
f = open(os.path.join(__location__, 'input'))

elves = {"elf1": 0}

elf_number = 1
for l in f:
    if l == "\n":
        elf_number += 1
        elves[f"elf{elf_number}"] = 0
        continue

    elves[f"elf{elf_number}"] += int(l)


print(f"solution a) {max(elves.values())}")

print(f"solution b) {sum(sorted(elves.values(), reverse=True)[:3])}")

f.close()

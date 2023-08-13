from pathlib import Path

input = [
    "$ cd /",
    "$ ls",
    "dir a",
    "14848514 b.txt",
    "8504156 c.dat",
    "dir d",
    "$ cd a",
    "$ ls",
    "dir e",
    "29116 f",
    "2557 g",
    "62596 h.lst",
    "$ cd e",
    "$ ls",
    "584 i",
    "$ cd ..",
    "$ cd ..",
    "$ cd d",
    "$ ls",
    "4060174 j",
    "8033020 d.log",
    "5626152 d.ext",
    "7214296 k",
]

import os
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

input = [l.strip() for l in open(os.path.join(__location__, 'input'))]

folders = {}

def create_dir():
    return {
        "folders": [],
        "files": {},
    }

def get_folder_size(name, folders):
    total = 0
    folder = folders[name]
    for _, size in folder["files"].items():
        total += int(size)
    for f in folder["folders"]:
        total += get_folder_size(f, folders)
    return total

for i, line in enumerate(input):
    if line == "$ cd /":
        path = Path("/")
    elif line.startswith("$ cd"):
        folder = line.split("$ cd ")[-1]
        path /= folder
    elif line.startswith("$ ls"):
        for line2 in input[i+1:]:
            if not line2.startswith("$"):
                if path.resolve() not in folders:
                    folders[path.resolve()] = create_dir()
                if not line2.startswith("dir"):
                    size, file = line2.split()
                    folders[path.resolve()]["files"][file] = size
                else:
                    folder2 = line2.split("dir ")[-1]
                    folders[path.resolve()]["folders"] += [(path / folder2).resolve()]
            else:
                break

p1 = 0
for name in folders:
    print(name)
    size = get_folder_size(name, folders)
    if size < 100000:
        p1 += size

print(p1)

total_space = 70000000 - get_folder_size(Path("/").resolve(), folders)
print(total_space)
best_name = ""
best_size = 999999999
for name in folders:
    size = get_folder_size(name, folders)
    if total_space + size >= 30000000:
        if size < best_size:
            best_name = name
            best_size = size

print(best_name, best_size)

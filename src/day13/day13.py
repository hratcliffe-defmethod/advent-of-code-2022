
# need to read input and separate each pairs for com-pair-ison

## Comparing rules
## First value is called left, second value is called right
## if both are integers, lower int comes first.
## If both values are lists, compare the first calue of each list, and so on. If left list runs out of items first, inputs are in the right order. If right list runs out of items firt, inputs are not in the right order..
from functools import cmp_to_key
from math import prod

TEST = False

def readInput(input):
    lines = open(inputFile).read().strip()
    pairs = [list(map(eval, p.split("\n"))) for p in lines.split("\n\n")]

    return pairs

def pretty_print(input):
    for item in input:
        print(item)

def compare_pair(pair1, pair2):
    left = pair1 if isinstance(pair1, list) else [pair1]
    right = pair2 if isinstance(pair2, list) else [pair2]

    for l2, r2 in zip(left, right):
        if isinstance(l2, list) or isinstance(r2, list):
            rec = compare_pair(l2, r2)
        else:
            rec = r2 - l2
        if rec != 0:
            return rec
    return len(right) - len(left)

if __name__ == "__main__":
    # TEST = True
    inputFile = "day13Sample.txt" if TEST else "day13Input.txt"
    pairs = readInput(inputFile)
    packets = sorted([y for x in pairs for y in x] + [[[2]], [[6]]], key=cmp_to_key(compare_pair), reverse=True)
    print(f"Part 1: {sum(i for i, (l, r) in enumerate(pairs, 1) if compare_pair(l, r) > 0)}")
    print(f"Part 2: {prod([n for n, packet in enumerate(packets, 1) if packet in ([[2]], [[6]])])}")
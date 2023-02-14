#!/usr/bin/env python3
def readFileLines():
    with open('day1Input.txt') as f:
        lines = f.readlines()
        elves = []
        current_elf_calories=0
        max_calories=0
        for line in lines:
            if line.strip('\n') == "":
                # append to list and reset current elf calories 
                elves.append(current_elf_calories)
                if current_elf_calories > max_calories:
                    max_calories = current_elf_calories
                current_elf_calories=0
            else:
                current_elf_calories = current_elf_calories + int(line)
        # use the max calories to get the elf
        elves.sort()
        elves_length = len(elves)
        sum = elves[elves_length-1] + elves[elves_length-2] + elves[elves_length-3]

        print(sum)

if name == '__main__':
    readFileLines()

TEST = False

def signal_strength(cycle, signal_register):
    return cycle * signal_register

if __name__ == "__main__":
    # TEST = True
    inputFile = "day10Sample.txt" if TEST else "day10Input.txt"
    instructions = open(inputFile).read().strip()
    signal_r_sums = []
    cycles = []
   
    # Part 1
    for line in instructions.split("\n"):
        cycles.extend([0] if line == "noop" else [0, int(line.split()[1])])
    for i in range(20, 221, 40):
        signal_r_sums.append(i * (sum(cycles[:i-1]) + 1))
    crt = [["."] * 40 for _ in range(6)]
    print(f"Part 1: {sum(signal_r_sums)}")

    # Part 2
    for c in range(len(cycles)):
        x = sum(cycles[:c]) + 1
        if c % 40 in range(x - 1, x + 2):
            crt[c//40][c%40] = "#"
    print("Part 2:")
    for line in crt:
        print("".join([p if p == "#" else " " for p in line]))
            
    

    

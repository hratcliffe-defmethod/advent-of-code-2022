def last_y(cave):
    return max(y for (_, y) in cave.keys())

def sand_fall(cave):
    x = 500 
 
    for y in range(last_y(cave)):
        # down one step
        if (x, y + 1) not in cave:
            continue 
        # down left 
        elif (x - 1, y + 1) not in cave:
            x -= 1
        # down right
        elif (x + 1, y + 1) not in cave:
            x += 1
        else: 
            cave[(x, y)] = "o"
            # stop simulation if we are blocked at starting position
            return (x, y) != (500, 0) 
    return False 

def add_bottom_floor(cave):
    y = last_y(cave) + 2
    for x in range(-1000, 1001):
        cave[(x, y)] = "#"
 
def simulate(has_bottom_floor):
    if has_bottom_floor:
        add_bottom_floor(cave)
 
    while sand_fall(cave):
        pass 
 
    return cave

if __name__ == "__main__":
    inputFile = open('day14Input.txt', 'r')
 
    lines = inputFile.read().strip().split("\n")
    
    cave = {}
    for line in lines:
        P = [x.split(",") for x in line.split("->")]
        points = [(int(x[0]), int(x[1])) for x in P]
    
        for p1, p2 in zip(points, points[1:]):
            x1, y1 = p1
            x2, y2 = p2
    
            for x in range(min(x1, x2), max(x1, x2) + 1):
                cave[(x, y1)] = "#"
    
            for y in range(min(y1, y2), max(y1, y2) + 1):
                cave[(x1, y)] = "#"
    # part 1
    p1 = sum(v == "o" for v in simulate(False).values())
    print(p1)
    
    p2 = sum(v == "o" for v in simulate(True).values())
    print(p2)

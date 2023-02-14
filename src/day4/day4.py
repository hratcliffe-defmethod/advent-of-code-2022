if __name__ == '__main__':
    data = open("day4Input.txt").read()
    p1 = p2 = 0
    for p in data.strip().split("\n"):
        r1 = range(int(p.split(",")[0].split("-")[0]), int(p.split(",")[0].split("-")[1]) + 1)
        r2 = range(int(p.split(",")[1].split("-")[0]), int(p.split(",")[1].split("-")[1]) + 1)
        if r1.start >= r2.start and r1.stop <= r2.stop or r2.start >= r1.start and r2.stop <= r1.stop:
            p1 += 1
        if set(r1).intersection(set(r2)):
            p2 += 1
    print(f"Part 1: {p1}")
    print(f"Part 2: {p2}")
    

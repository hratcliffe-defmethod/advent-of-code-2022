def get_priority_value(v):
    priority = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    return priority.index(v) + 1

def readInput():
    priority_sum = 0
    with open('day3.txt') as f:
        lines = f.readlines()
        line_group = []
        for line in lines:
            line_group.append(set(line.strip('\n')))
            if len(line_group) == 3:
                badge = set(line_group[0]) & set(line_group[1]) & set(line_group[2])
                print(badge)
                priority_sum = priority_sum + get_priority_value(badge.pop())
                line_group = []
    return priority_sum

if __name__ == '__main__':
    sum = readInput()
    print(sum)
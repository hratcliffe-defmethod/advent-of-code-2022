TEST = False

def processInput(lines):
    monkeys = {}
    for line in lines:
        split = line.strip().split(":")
        monkey_name = split[0].strip()
        monkey_num = split[1].strip()
        monkeys[monkey_name] = monkey_num
    return monkeys


def getMonkeyValue(monkeys, monkey_val, monkey_name=""):
    monkey_value = ""

    if monkey_name == "root":
        names = monkey_val.split("+")
        first_monkey_name = names[0].strip()
        second_monkey_name = names[1].strip()
        monkey_value = getMonkeyValue(monkeys, monkeys[first_monkey_name]) == getMonkeyValue(monkeys, monkeys[second_monkey_name])
    elif "+" in monkey_val:
        names = monkey_val.split("+")
        first_monkey_name = names[0].strip()
        second_monkey_name = names[1].strip()
        monkey_value = getMonkeyValue(monkeys, monkeys[first_monkey_name]) + getMonkeyValue(monkeys, monkeys[second_monkey_name])
    elif "*" in monkey_val:
        names = monkey_val.split("*")
        first_monkey_name = names[0].strip()
        second_monkey_name = names[1].strip()
        monkey_value = getMonkeyValue(monkeys, monkeys[first_monkey_name]) * getMonkeyValue(monkeys, monkeys[second_monkey_name])
    elif "/" in monkey_val:
        names = monkey_val.split("/")
        first_monkey_name = names[0].strip()
        second_monkey_name = names[1].strip()
        monkey_value = getMonkeyValue(monkeys, monkeys[first_monkey_name]) / getMonkeyValue(monkeys, monkeys[second_monkey_name])
    elif "-" in monkey_val:
        names = monkey_val.split("-")
        first_monkey_name = names[0].strip()
        second_monkey_name = names[1].strip()
        monkey_value = getMonkeyValue(monkeys, monkeys[first_monkey_name]) - getMonkeyValue(monkeys, monkeys[second_monkey_name])
    else:
        monkey_value = monkey_val
    
    return int(monkey_value)

if __name__ == "__main__":
    # TEST = True
    inputFile = "day21Sample.txt" if TEST else "day21Input.txt"
    with open(inputFile) as f:
        lines = f.readlines()
        monkeys = processInput(lines)

        # will need to do some recursion to check the monkeys. Eventually we should hit every monkey
        final = -1
        for i in range(3509819803064, 3509819803066):
            monkeys['humn'] = str(i)
            val = getMonkeyValue(monkeys, monkeys['root'], "root")
            if val == 1:
                final = i
                break
        print(final)
    





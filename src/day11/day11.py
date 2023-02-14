class Monkey():
    indent_int: int
    items: list
    op_value: int
    op: str
    div_val: int
    true_monkey: int
    false_monkey: int

    def __init__(self, iden, items, op, op_val, div_val, true, false):
        self.indent_int = iden
        self.items = items
        self.op = op
        self.op_value = op_val
        self.div_val = div_val
        self.true_monkey = true
        self.false_monkey = false

    def add_item(self, item):
        self.items.append(item)

    def inspect(self, item):
        if self.op == "*":
            return item * self.op_value
        elif self.op == "+":
            return item + self.op_value
        elif self.op == "sq":
            return item * item
    
    def test(self, item):
        if item % self.div_val == 0:
            return self.true_monkey
        return self.false_monkey

if __name__ == '__main__':
    monkey0 = Monkey(0, [53, 89, 62, 57, 74, 51, 83, 97], "*", 3, 13, 1, 5)
    monkey1 = Monkey(1, [85, 94, 97, 92, 56], "+", 2, 19, 5, 2)
    monkey2 = Monkey(2, [86, 82, 82], "+", 1, 11, 3, 4)
    monkey3 = Monkey(3, [94, 68], "+", 5, 17, 7, 6)
    monkey4 = Monkey(4, [83, 62, 74, 58, 96, 68, 85], "+", 4, 3, 3, 6)
    monkey5 = Monkey(5, [50, 68, 95, 82], "+", 8, 7, 2, 4)
    monkey6 = Monkey(6, [75], "*", 7, 5, 7, 0)
    monkey7 = Monkey(7, [92, 52, 85, 89, 68, 82], "sq", 0, 2, 0, 1)
    monkeys = [monkey0, monkey1, monkey2, monkey3, monkey4, monkey5, monkey6, monkey7]
    monkey_inspections = [0, 0, 0, 0, 0, 0, 0, 0]

    rounds = 10000

    super_modulos = []
    super_modulo_value = 1
    for monkey in monkeys:
        super_modulos.append(monkey.div_val)
    for value in super_modulos:
        super_modulo_value *= value

    for i in range(0, rounds):
        for monkey in monkeys:
            length_starting_items = len(monkeys[monkey.indent_int].items)
            for i in range(length_starting_items):
                monkey_inspections[monkey.indent_int] += 1
                item = monkey.items.pop(0) % super_modulo_value
                item = monkey.inspect(item)
                monkey_to_throw_to = monkey.test(item)
                monkeys[monkey_to_throw_to].add_item(item)
    sorted_inspections = sorted(monkey_inspections)
    print(sorted_inspections)
    monkey_business = sorted_inspections[-1] * sorted_inspections[-2]
    print(monkey_business)

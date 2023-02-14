
def readInput(filename):
    with open(filename) as f:
        lines = f.readlines()
        stacks = [[],[],[],[],[],[],[],[],[]]
        moves = []
        for line in lines:
            if line == "\n":
                continue
            # Parse all moves
            if line[0:4] == 'move':
                for c in ['move', 'from', 'to']: line = line.replace(c, "-")
                for c in [" ", "\n"]: line = line.replace(c, "")
                current_moves = line.split('-')
                current_moves.pop(0)
                moves.append([int(current_moves[0]), int(current_moves[1]), int(current_moves[2])])
            else:
                # handle the stacks starting state
                line = line.replace("[", " ").replace("]", " ")
                stack_num = 0
                for i in range(1, len(line)-1, 4):
                    if line[i] != ' ' and line[i] != '\n' and line[i] not in ['0','1','2','3','4','5','6','7','8','9']:
                        stacks[stack_num].append(line[i])
                    stack_num += 1
        return stacks, moves

def process_moves(moves, stacks):
    for move_set in moves:
        num_items, stack_from, stack_to = move_set
        stacks = make_move(stacks, num_items, stack_from, stack_to)
    return stacks

def make_move(stacks, num_items, stack_from, stack_to):
    items_being_moved = []
    for i in range(num_items):
        if len(stacks[stack_from-1]) > 0:
            item = stacks[stack_from-1].pop(0) 
            items_being_moved.append(item)
    stacks[stack_to-1] = items_being_moved + stacks[stack_to-1]
    return stacks

def get_top_items(stacks):
    top_items = ''.join([stack[0] if len(stack)>0 else "" for stack in stacks])
    return top_items

if __name__ == '__main__':
    stacks, moves = readInput('day5Input.txt')
    # stacks, moves = readInput('day5Sample.txt')
    new_stacks = process_moves(moves, stacks)
    items = get_top_items(new_stacks)
    print(items)
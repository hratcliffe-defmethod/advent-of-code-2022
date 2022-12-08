TEST = False
import timeit

def process_grid_input(input):
    grid = []
    for line in input:
        tree_line = list(map(int, line.strip()))
        grid.append(tree_line)
    return grid

### Part 1: Visibility
def visible_north(grid, tree_y, tree_x):
    # when looking north, we look at the trees for 0 -> tree_y
    for y in range(0, tree_y):
        if grid[y][tree_x] >= grid[tree_y][tree_x]:
            return False
    return True        

def visible_west(grid, tree_y, tree_x):
    # when looking west, we look at the trees for 0 -> tree_x
    for x in range(0, tree_x):
        if grid[tree_y][x] >= grid[tree_y][tree_x]:
            return False
    return True        

def visible_south(grid, tree_y, tree_x):
    # when looking south, we look at the trees from tree_y -> end of grid y
    for y in range(tree_y+1, len(grid)):
        if grid[y][tree_x] >= grid[tree_y][tree_x]:
            return False
    return True        

def visible_east(grid, tree_y, tree_x):
    # when looking east, we look at the trees from tree_x -> end of grid x
    for x in range(tree_x+1, len(grid[tree_y])):
        if grid[tree_y][x] >= grid[tree_y][tree_x]:
            return False
    return True     

### Part 2: Scenic Multiplier
def scenic_north(grid, tree_y, tree_x):
    score = 0
    # when looking north, we look at the trees from tree_y -> 0
    for y in range(tree_y-1, -1, -1):
        current_tree = grid[tree_y][tree_x]
        if grid[y][tree_x] < current_tree:
            score = score + 1
        elif grid[y][tree_x] >= current_tree:
            score = score + 1
            return score
    return score       

def scenic_west(grid, tree_y, tree_x):
    score = 0
    # when looking west, we look at the trees from tree_x -> 0
    for x in range(tree_x-1, -1, -1):
        current_tree = grid[tree_y][tree_x]
        if grid[tree_y][x] < current_tree:
            score = score + 1
        elif grid[tree_y][x] >= current_tree:
            score = score + 1
            return score
    return score         

def scenic_south(grid, tree_y, tree_x):
    score = 0
    # when looking south, we look at the trees from tree_y -> end of grid y
    for y in range(tree_y+1, len(grid)):
        current_tree = grid[tree_y][tree_x]
        if grid[y][tree_x] < current_tree:
            score = score + 1
        elif grid[y][tree_x] >= current_tree:
            score = score + 1
            return score
    return score     

def scenic_east(grid, tree_y, tree_x):
    score = 0
    # when looking east, we look at the trees from tree_x -> end of grid x
    for x in range(tree_x+1, len(grid[tree_y])):
        current_tree = grid[tree_y][tree_x]
        if grid[tree_y][x] < current_tree:
            score = score + 1
        elif grid[tree_y][x] >= current_tree:
            score = score + 1
            return score
    return score     


def get_visible_and_scenic(grid):
    exterior_visible = (len(grid)*2) + ((len(grid)-2)*2)
    interior_visible = 0
    highest_scenic_score = 0

    for y in range(1, len(grid)-1):
        for x in range(1, len(grid[y])-1):
            ### Part 1
            if visible_north(grid, y, x) or visible_east(grid, y, x) or visible_south(grid, y, x) or visible_west(grid, y, x):
                interior_visible = interior_visible + 1
            ### Part 2
            current_tree_score = scenic_north(grid, y, x) * scenic_south(grid, y, x) * scenic_east(grid, y, x) * scenic_west(grid, y, x)
            if current_tree_score > highest_scenic_score:
                highest_scenic_score = current_tree_score

    return exterior_visible + interior_visible, highest_scenic_score

if __name__ == "__main__":
    # TEST = True
    inputFile = 'day8Sample.txt' if TEST else 'day8Input.txt'
    with open(inputFile) as file:
        grid_data = file.readlines()
        grid = process_grid_input(grid_data)

        visible_sum, scenic_max = get_visible_and_scenic(grid)
        print(f"visible_sum: {visible_sum}\nscenic_max: {scenic_max}")



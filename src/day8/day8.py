TEST = False

def process_grid_input(input):
    grid = []
    for line in input:
        tree_line = list(map(int, line.strip()))
        grid.append(tree_line)
    return grid

### Part 1: Visibility
def is_visible(grid: list, tree_y: int, tree_x: int, loop_range: list, NS: bool):
    for index in range(loop_range[0], loop_range[1]):
        if grid[index if NS else tree_y][index if not NS else tree_x] >= grid[tree_y][tree_x]:
            return False
    return True 

### Part 2: Scenic Multiplier 
def scenic_score(grid: list, tree_y: int, tree_x: int, loop_range: list, NS: bool, step=1):
    score = 0
    for index in range(loop_range[0], loop_range[1], loop_range[2]):
        current_tree = grid[tree_y][tree_x]
        adj_tree = grid[index if NS else tree_y][index if not NS else tree_x]
        if adj_tree < current_tree:
            score = score + 1
        elif adj_tree >= current_tree:
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
            north_visible = is_visible(grid, y, x, [0, y], True)
            south_visible = is_visible(grid, y, x, [y+1, len(grid)], True)
            east_visible = is_visible(grid, y, x, [x+1, len(grid[y])], False)
            west_visible = is_visible(grid, y, x, [0, x], False)

            if north_visible or south_visible or east_visible or west_visible:
                interior_visible = interior_visible + 1

            ### Part 2
            north_score = scenic_score(grid, y, x, [y-1, -1, -1], True)
            south_score = scenic_score(grid, y, x, [y+1, len(grid[y]), 1], True)
            east_score = scenic_score(grid, y, x, [x+1, len(grid[y]), 1], False)
            west_score = scenic_score(grid, y, x, [x-1, -1, -1], False)
            
            current_tree_score = north_score * south_score * east_score * west_score

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



# day 9

class Knot:
    def __init__(self):
        self.x = 0
        self.y = 0

    @property
    def pos(self):
        return self.x, self.y

class Head(Knot):
    def step(self, direction):
        # move 1 step in the direction

        if direction == 'U':
            self.y += 1
        if direction == 'D':
            self.y -= 1
        if direction == 'L':
            self.x -= 1
        if direction == 'R':
            self.x += 1


class Tail(Knot):
    def __init__(self):
        super().__init__()
        self.history = set()

    def follow(self, pos):
        x, y = pos
        dist_x = x - self.x
        dist_y = y - self.y
        if abs(dist_x) == 2 and not dist_y: # horizontal
            xv = 1 if dist_x > 0 else -1
            self.x += xv
        elif abs(dist_y) == 2 and not dist_x: # vertical
            yv = 1 if dist_y > 0 else -1
            self.y += yv
        elif (abs(dist_y) == 2 and abs(dist_x) in (1, 2)) or (abs(dist_x) == 2 and abs(dist_y) in (1, 2)):
            xv = 1 if dist_x > 0 else -1
            self.x += xv
            yv = 1 if dist_y > 0 else -1
            self.y += yv
        self.history.add((self.x, self.y))


head = Head()
tail = Tail()
with open('day9Input.txt') as f:
    directions = f.read().splitlines()

for direction in directions:
    dir_, steps = direction.split()
    for _ in range(int(steps)):
        head.step(dir_)
        tail.follow(head.pos)
print(f"Part 1: Number of positions visited: {len(tail.history)}")

# part 2
head = Head()
tails = [Tail() for _ in range(9)]
for direction in directions:
    dir_, steps = direction.split()
    for _ in range(int(steps)):
        head.step(dir_)
        tails[0].follow(head.pos)
        for i in range(1, 9):
            tails[i].follow(tails[i-1].pos)
print(f"Part 2: Number of positions visited: {len(tails[8].history)}")


### First solution, unsuccessful, keeping for records
# def grid_viz(grid):
#     top = '['
#     for i in range(0, len(grid)):
#         top = top + f"'{i}', "
#     top = top + "]"

#     print(top)
#     for row in grid:
#         print(row) 

# class Knot:
#     knot_name: str
#     x_pos: int
#     y_pos: int
#     parent_knot: None
#     child_knot: None

#     def __init__(self, name: str, x_pos: int, y_pos: int, parent=None, child=None):
#         self.knot_name = name
#         self.x_pos = x_pos
#         self.y_pos = y_pos
#         self.parent_knot = parent
#         self.child_knot = child

#     def setChild(self, child):
#         self.child_knot = child
    
#     def get_position(self):
#         return [self.y_pos, self.x_pos]

#     def update_pos(self, y, x, grid):
#         # grid[self.y_pos][self.x_pos] = self.knot_name
#         print(self.y_pos, self.x_pos)
#         self.y_pos = self.y_pos + y
#         self.x_pos = self.x_pos + x

#         # if self.child_knot:
#         #     if direction == "U":
#         #         return self.child_knot.check_north(grid, direction)
#         #     elif direction == "D":
#         #         return self.child_knot.check_south(grid, direction)
#         #     elif direction == "R":
#         #         return self.child_knot.check_east(grid, direction)
#         #     elif direction == "L":
#         #         return self.child_knot.check_west(grid, direction)
#         return grid

#     def check_south(self, grid):
#         # check tail adjacency S, SE, SW. If none, its moved out of range and we need to catch up
#         if self.get_position() == self.parent_knot.get_position():
#             grid[self.y_pos][self.x_pos] = self.knot_name
#         elif [self.y_pos+1, self.x_pos] != self.parent_knot.get_position() and [self.y_pos+1, self.x_pos-1] != self.parent_knot.get_position() and [self.y_pos+1, self.x_pos+1] != self.parent_knot.get_position():
#             # check diagonal direction
#             grid[self.y_pos][self.x_pos] = self.knot_name
#             if self.y_pos+2 == self.parent_knot.y_pos and self.x_pos+1 == self.parent_knot.x_pos: # move tail diagonally SE
#                 grid = self.update_pos(1, 1, grid)
#             elif self.y_pos+2 == self.parent_knot.y_pos and self.x_pos-1 == self.parent_knot.x_pos: # move tail diagonally SW
#                 grid = self.update_pos(1, -1,  grid)
#             elif self.y_pos+2 == self.parent_knot.y_pos and self.x_pos == self.parent_knot.x_pos: # move tail S
#                 grid = self.update_pos(1, 0, grid)
#         return grid

#     def check_north(self, grid):
#         if self.get_position() == self.parent_knot.get_position():
#             grid[self.y_pos][self.x_pos] = self.knot_name
#         elif [self.y_pos-1, self.x_pos] != self.parent_knot.get_position() and [self.y_pos-1, self.x_pos-1] != self.parent_knot.get_position() and [self.y_pos-1, self.x_pos+1] != self.parent_knot.get_position():
#             grid[self.y_pos][self.x_pos] = self.knot_name
#             # check diagonal direction
#             if self.y_pos-2 == self.parent_knot.y_pos and self.x_pos+1 == self.parent_knot.x_pos: # move tail diagonally NE
#                 grid = self.update_pos(-1, 1, grid)
#             elif self.y_pos-2 == self.parent_knot.y_pos and self.x_pos-1 == self.parent_knot.x_pos: # move tail diagonally NW
#                 grid = self.update_pos(-1, -1, grid)
#             elif self.y_pos-2 == self.parent_knot.y_pos and self.x_pos == self.parent_knot.x_pos: # move tail N
#                 grid = self.update_pos(-1, 0, grid)
#         return grid
   
#     def check_east(self, grid):
#         # check tail adjacency E, NE, SE. If none, its moved out of range and we need to catch up
#         if self.get_position() == self.parent_knot.get_position():
#             grid[self.y_pos][self.x_pos] = self.knot_name
#         elif [self.y_pos, self.x_pos+1] != self.parent_knot.get_position() and [self.y_pos+1, self.x_pos+1] != self.parent_knot.get_position() and [self.y_pos-1, self.x_pos+1] != self.parent_knot.get_position():
#             grid[self.y_pos][self.x_pos] = self.knot_name
#             # check diagonal direction
#             if self.y_pos-1 == self.parent_knot.y_pos and self.x_pos+2 == self.parent_knot.x_pos: # move tail diagonally NE
#                 grid = self.update_pos(-1, 1, grid)
#             elif self.y_pos+1 == self.parent_knot.y_pos and self.x_pos+2 == self.parent_knot.x_pos: # move tail diagonally SE
#                 grid = self.update_pos(1, 1, grid)
#             elif self.y_pos == self.parent_knot.y_pos and self.x_pos+2 == self.parent_knot.x_pos: # move tail E
#                 grid = self.update_pos(0, 1, grid)
#         return grid

#     def check_west(self, grid):
#          # check tail adjacency W, NW, SW. If none, its moved out of range and we need to catch up
#         if self.get_position() == self.parent_knot.get_position():
#             grid[self.y_pos][self.x_pos] = self.knot_name
#         elif [self.y_pos, self.x_pos-1] != self.parent_knot.get_position() and [self.y_pos+1, self.x_pos-1] != self.parent_knot.get_position() and [self.y_pos-1, self.x_pos-1] != self.parent_knot.get_position():
#             # check diagonal direction
#             grid[self.y_pos][self.x_pos] = self.knot_name
#             if self.y_pos-1 == self.parent_knot.y_pos and self.x_pos-2 == self.parent_knot.x_pos: # move tail diagonally NW
#                 grid = self.update_pos(-1, -1, grid)
#             elif self.y_pos+1 == self.parent_knot.y_pos and self.x_pos-2 == self.parent_knot.x_pos: # move tail diagonally SW
#                 grid = self.update_pos(1, -1, grid)
#             elif self.y_pos == self.parent_knot.y_pos and self.x_pos-2 == self.parent_knot.x_pos: # move tail W
#                 grid = self.update_pos(0, -1, grid)
#         return grid


# if __name__ == "__main__":
#     TEST = True
#     size = 100
#     grid = [["0" for y in range(0, size)] for i in range(0, size)]
#     starting_point = [int(size/2), int(size/2)] #start in the middle

#     inputFile = 'day9Sample.txt' if TEST else 'day9Input.txt'
#     # size = 500
#     # grid = [[" " for y in range(0, size)] for i in range(0, size)]
#     # starting_point = [int(size/2), int(size/2)] #start in the middle
#     # starting_point = [50, 50]

#     knots = []
#     for i in range(0, 9):
#         parent = None
#         if i != 0:
#             parent = knots[i-1]
#         else:
#             parent = None
#         knot = Knot(str(i), starting_point[0], starting_point[1], parent)
#         if parent:
#             parent.setChild(knot)
#         knots.append(knot)
#     head = knots[0]
    
#     with open(inputFile) as file:
#         instructions = file.readlines()
#         for i in instructions:
#             direction, spaces = i.split(' ')
#             spaces = int(spaces)

#             if direction == "D":
#                 for i in range(0, spaces):
#                     grid = head.update_pos(1, 0, grid)
#                     for knot in knots:
#                         # update each knot individually, return the grid and continue. Do not call recursively
#                         # check the parent, then update
#                         # call child to update
#                         if knot.child_knot:
#                             grid = knot.child_knot.check_south(grid)
#             elif direction == "U": 
#                 for i in range(0, spaces):
#                     grid = head.update_pos(-1, 0, grid)
#                     for knot in knots:
#                         # update each knot individually, return the grid and continue. Do not call recursively
#                         # check the parent, then update
#                         # call child to update
#                         if knot.child_knot:
#                             grid = knot.child_knot.check_north(grid)
#             elif direction == "L":
#                 for i in range(0, spaces):
#                     grid = head.update_pos(0, -1, grid)
#                     for knot in knots:
#                         # update each knot individually, return the grid and continue. Do not call recursively
#                         # check the parent, then update
#                         # call child to update
#                         if knot.child_knot:
#                             grid = knot.child_knot.check_west(grid)
#             elif direction == "R":
#                 for i in range(0, spaces):
#                     grid = head.update_pos(0, 1, grid)
#                     for knot in knots:
#                         if knot.child_knot:
#                             grid = knot.child_knot.check_east(grid)
#         count = 0
#         for x in range(0, len(grid)):
#             for y in range(0, len(grid)):
#                 if grid[x][y] == '8':
#                     count += 1
#         grid_viz(grid)
#         print(count)

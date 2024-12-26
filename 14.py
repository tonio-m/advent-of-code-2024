import re
from pprint import pprint

# s = """p=0,4 v=3,-3
# p=6,3 v=-1,-3
# p=10,3 v=-1,2
# p=2,0 v=2,-1
# p=0,0 v=1,3
# p=3,0 v=-2,-2
# p=7,6 v=-1,-3
# p=3,0 v=-1,-2
# p=9,3 v=2,3
# p=7,3 v=-1,2
# p=2,4 v=2,-3
# p=9,5 v=-3,-3
# """
s = open('14.txt','r').read()

positions = list(map(int,re.findall(r'-?\d+',s)))
positions = [positions[i:i+4] for i in range(0, len(positions), 4)]

def make_grid(rows,cols):
    return [[0] * cols for i in range(rows)]

def displace(positions,grid):
    new_positions = []
    for p_x,p_y,v_x,v_y in positions:
        new_positions.append(
            [
                (p_x + v_x * 100) % len(grid[0]),
                (p_y + v_y * 100) % len(grid),
                v_x,
                v_y
            ]
        )
    return new_positions

def place(positions,grid):
    for p_x,p_y,v_x,v_y in positions:
        grid[p_y][p_x] += 1
    return

def print_grid(grid):
    [print(''.join([str(i) if i else '.' for i in row])) for row in grid]

def quadrants_score(grid):
    rows = len(grid)
    cols = len(grid[0])
    q1 = [row[:cols//2] for row in grid[:rows//2]]
    q2 = [row[cols//2 + 1:] for row in grid[:rows//2]]
    q3 = [row[:cols//2] for row in grid[rows//2 + 1:]]
    q4 = [row[1 + cols//2:] for row in grid[1 + rows//2:]]

    # print_grid(q1)
    # print('')
    # print_grid(q2)
    # print('')
    # print_grid(q3)
    # print('')
    # print_grid(q4)
    # print('')

    return (sum([sum(x) for x in q1]) *
    sum([sum(x) for x in q2]) *
    sum([sum(x) for x in q3]) *
    sum([sum(x) for x in q4]))

grid = make_grid(103,101)
new_positions = displace(positions,grid)
place(new_positions,grid)
print(quadrants_score(grid))


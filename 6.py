# part 1
from tqdm import tqdm
from copy import deepcopy
import pdb
from time import sleep
from pprint import pprint

# s = """....#.....
# .........#
# ..........
# ..#.......
# .......#..
# ..........
# .#..^.....
# ........#.
# #.........
# ......#...
# """

s = open('6.txt','r').read()

t = [list(l) for l in s.split('\n')][:-1]

def get_cur_pos(t):
    for y in range(len(t)):
        for x in range(len(t[y])):
            c = t[y][x]
            if c == '^':
                return (y,x)
    return None

def rotate_90_right(x, y):
    return (y, -x)

def walk(t,cur_pos,direction):
    y,x = cur_pos
    y_n,x_n = (y + direction[0], x + direction[1])

    while True:
        if x_n < 0 or y_n < 0 or x_n >= len(t[y]) or y_n >= len(t):
            t[y][x] = 'X'
            break
        elif t[y_n][x_n] == '#':
            direction =  rotate_90_right(*direction)
            y_n,x_n = (y + direction[0], x + direction[1])
        else:
            t[y][x] = 'X'
            t[y_n][x_n] = '^'
            y, x = (y_n,x_n)
            y_n,x_n = (y + direction[0], x + direction[1])
        # print("\033[H\033[J", end="")
        # pprint(t)
        # sleep(0.1)
    return t

direction = (-1,0)
cur_pos = get_cur_pos(t)
t_ = deepcopy(t)
t_ = walk(t_,cur_pos,direction)
print(''.join([''.join(l) for l in t_]).count('X'))

# part 2
def walk_check_loop(t,cur_pos,direction):
    y,x = cur_pos
    y_n,x_n = (y + direction[0], x + direction[1])

    collisions = []

    o_hits = 0
    while True:
        if x_n < 0 or y_n < 0 or x_n >= len(t[y]) or y_n >= len(t):
            t[y][x] = 'X'
            break
        elif t[y_n][x_n] == '#':
            collisions.append((direction, (y_n, x_n)))
            if o_hits > 0 and (direction, (y_n, x_n)) in collisions[:-1]:
                return True
            direction =  rotate_90_right(*direction)
            y_n,x_n = (y + direction[0], x + direction[1])
        elif t[y_n][x_n] == 'O':
            direction =  rotate_90_right(*direction)
            y_n,x_n = (y + direction[0], x + direction[1])
            o_hits += 1
            if o_hits >= 3: return True
        else:
            t[y][x] = 'X'
            t[y_n][x_n] = '^'
            y, x = (y_n,x_n)
            y_n,x_n = (y + direction[0], x + direction[1])
        # print("\033[H\033[J", end="")
        # [print(''.join(l)) for l in t]
        # sleep(0.001)
    return False


direction = (-1,0)
cur_pos = get_cur_pos(t)
hits = []
for y in range(len(t)):
    for x in range(len(t[y])):
        t_ = deepcopy(t)
        t_[y][x] = 'O'
        hits.append(walk_check_loop(t_,cur_pos,direction))

print(hits.count(True))


# part 1
import pdb

s = open('10.txt','r').read()

t = [list(map(int,l)) for l in s.split('\n')[:-1]]

def get_neighbors(x,y,x_max,y_max):
    neighbors = []
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    for x_a,y_a in directions:
        x_n = x + x_a
        y_n = y + y_a
        if 0 <= x_n < x_max and 0 <= y_n < y_max:
            neighbors.append((x_n,y_n))
    return neighbors

def find_trailheads(t):
    heads = []
    for y in range(len(t)):
        for x in range(len(t[0])):
            if t[y][x] == 0:
                heads.append((x,y))
    return heads


def trailhead_score(t,head):
    queue = [head]
    rows = len(t)
    cols = len(t[0])
    summits = []

    while len(queue):
        x,y = queue.pop()
        value = t[y][x]

        # print(f'{(x,y)=},{value=},{summits=},{queue=}')
        # pdb.set_trace()

        if value == 9 and (x,y) not in summits:
            summits.append((x,y))

        for x_neighbor, y_neighbor in get_neighbors(x,y,cols,rows):
            value_neighbor = t[y_neighbor][x_neighbor]
            if value_neighbor == value + 1:
                queue.append((x_neighbor,y_neighbor))
    return len(summits)

heads = find_trailheads(t)
print(sum([trailhead_score(t,head) for head in heads]))

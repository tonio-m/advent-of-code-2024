# part 1
# s = """RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
# """

s = open("12.txt","r").read()

t = [list(l) for l in s.split('\n')[:-1]]

def get_neighbors(x,y,x_max,y_max):
    neighbors = []
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    for x_a,y_a in directions:
        x_n = x + x_a
        y_n = y + y_a
        if 0 <= x_n < x_max and 0 <= y_n < y_max:
            neighbors.append((x_n,y_n))
    return neighbors

def get(t,x,y):
    if x >= len(t[0]) or x < 0 or y >= len(t) or y < 0:
        return None
    return t[y][x]

def get_edges(t,x,y):
    e = 0
    char = t[y][x].upper()
    directions = [(1,0),(0,1),(-1,0),(0,-1)]
    for x_a,y_a in directions:
        x_n = x + x_a
        y_n = y + y_a
        if get(t,x_n,y_n) not in (char,char.lower()):
            e += 1
    return e

def fill(t,init_pos,char):
    tile_count = 0
    edge_count = 0
    queue = [init_pos]
    rows, cols = len(t[0]), len(t)
    already_visited = []

    while queue:
        x,y = queue.pop(0)

        tile_count += 1
        edge_count += get_edges(t,x,y)

        t[y][x] = t[y][x].lower()
        already_visited.append((x,y))
        # print("\033[H\033[J" + "  0123456789")
        # [print(f"{y} {''.join(l)}") for y, l in enumerate(t)]
        # print((x,y))
        # sleep(0.1)
        # pdb.set_trace()

        for x_n,y_n in get_neighbors(x,y,rows,cols):
            if t[y_n][x_n] == char and (x_n,y_n) not in queue:
                queue.append((x_n,y_n))


    return (tile_count,edge_count)

def iterate(t):
    counts = []
    for y in range(len(t)):
        for x in range(len(t[0])):
            if t[y][x] == t[y][x].lower():
                continue
            else:
                char = t[y][x]
                counts.append((char,fill(t,(x,y),char)))
    print(sum([nums[0] * nums[1] for char, nums in counts]))


iterate(t)

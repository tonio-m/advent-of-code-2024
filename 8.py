# part 1
import pdb
import itertools
from pprint import pprint

# s = """......#....#
# ...#....0...
# ....#0....#.
# ..#....0....
# ....0....#..
# .#....A.....
# ...#........
# #......#....
# ........A...
# .........A..
# ..........#.
# ..........#.
# """

s = open('8.txt','r').read()

t = [list(l) for l in s.split('\n')[:-1]]

def vector_subtraction(a,b):
    return [a[i] - b[i] for i in range(len(a))]

def is_double(list1, list2):
    return all(x*2 == y for x, y in zip(list1, list2)) or all(x == y*2 for x, y in zip(list1, list2))

def remove_antinodes(t):
    for y in range(len(t)):
        for x in range(len(t[y])):
            if t[y][x] == '#':
                t[y][x] = '.'
    return t

def get_antennas_dict(t):
    antenna_locations = {}
    for y in range(len(t)):
        for x in range(len(t[y])):
            value = t[y][x]
            if value not in '.#':
                antenna_locations.setdefault(value, []).append((x,y))
    return antenna_locations

def is_antinode(current_node,antenna_locations):
    for antenna_1, antenna_2 in itertools.combinations(antenna_locations,2): 
        distance_1 = vector_subtraction(current_node,antenna_1)
        distance_2 = vector_subtraction(current_node,antenna_2)
    
        if is_double(distance_1,distance_2):
            return True

def get_antinodes(t,antenna_locations_dict):
    for y in range(len(t)):
        for x in range(len(t[y])):
            current_node = (x,y)
            for char, locations in antenna_locations_dict.items():
                if is_antinode(current_node,locations):
                    t[y][x] = '#'

remove_antinodes(t)
antennas = get_antennas_dict(t)
get_antinodes(t,antennas)
print(sum([l.count('#')for l in t]))

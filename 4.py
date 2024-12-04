# part 1
s = open('4.txt','r').read()
t = [list(l) for l in s.split('\n')][:-1]

def vertical_slice(list_,x,y_start,y_end):
    return [l[x] for l in list_[y_start:y_end]]

def count_xmas(t):
    c = 0
    for y in range(len(t)):
        for x in range(len(t[y])):
            # normal
            if t[y][x] == 'X' and x + 3 < len(t[y]) and ''.join(t[y][x:x+4]) == 'XMAS':
                c+=1
    
            # backward!
            elif t[y][x] == 'S' and x + 3 < len(t[y]) and ''.join(t[y][x:x+4]) == 'SAMX':
                c+=1
    
            # vertical!
            if t[y][x] == 'X' and y + 3 < len(t) and ''.join(vertical_slice(t,x,y,y+4)) == 'XMAS':
                c+=1
    
            # vertical backward!
            elif t[y][x] == 'S' and y + 3 < len(t) and ''.join(vertical_slice(t,x,y,y+4)) == 'SAMX':
                c+=1
    
            # diagonal!
            if t[y][x] == 'X' and y + 3 < len(t) and x + 3 < len(t) and t[y][x] + t[y+1][x+1] + t[y+2][x+2] + t[y+3][x+3] == 'XMAS':
                c+=1
    
            # diagonal backward!
            elif t[y][x] == 'S' and y + 3 < len(t) and x + 3 < len(t) and t[y][x] + t[y+1][x+1] + t[y+2][x+2] + t[y+3][x+3] == 'SAMX':
                c+=1
    
            # diagonal upward!
            if t[y][x] == 'X' and y - 3 >= 0 and x + 3 < len(t) and t[y][x] + t[y-1][x+1] + t[y-2][x+2] + t[y-3][x+3] == 'XMAS':
                c+=1
    
            # diagonal upward backward!
            elif t[y][x] == 'S' and y - 3 >= 0 and x + 3 < len(t) and t[y][x] + t[y-1][x+1] + t[y-2][x+2] + t[y-3][x+3] == 'SAMX':
                c+=1
    return c

print(count_xmas(t))

# part 2
def count_crossed_mas(t):
    c = 0
    for y in range(len(t)):
        for x in range(len(t[y])):
            boundary_check = (y - 1 >= 0) and (y + 1 < len(t)) and (x + 1 < len(t[y])) and (x - 1 >= 0)

            if t[y][x] == 'A' and boundary_check:
                left_mas = t[y-1][x-1] + t[y][x] + t[y+1][x+1]
                right_mas = t[y+1][x-1] + t[y][x] + t[y-1][x+1]
                if  left_mas in ('MAS','SAM') and right_mas in ('MAS','SAM'):
                    c+=1
    return c

print(count_crossed_mas(t))

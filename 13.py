# part 1
import re

# s = '''Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=8400, Y=5400
# 
# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=12748, Y=12176
# 
# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=7870, Y=6450
# 
# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=18641, Y=10279
# '''

s = open('13.txt','r').read()[:-1]

s = [list(map(int,re.findall(r'\d+',text))) for text in s.split('\n\n')] 

def solve(a_x,a_y,b_x,b_y,prize_x,prize_y):
    presses = []
    for b_presses in range(101):
        for a_presses in range(101):
            if (a_x * a_presses + b_x * b_presses) == prize_x and (a_y * a_presses + b_y * b_presses) == prize_y:
                   presses.append((a_presses,b_presses))

    min_score = float("infinity")
    for a_presses, b_presses in presses:
        score = a_presses * 3 + b_presses * 1
        if  score < min_score:
            min_score = score
    return min_score


solutions = [solve(*p) for p in s]

print(sum([sol for sol in solutions if sol != float("infinity")]))


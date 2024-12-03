# part 1
t = open('2.txt','r').read()
t_lists = [list(map(int,line.split())) for line in t.split('\n')][:-1]
def check(l):
    n_last = l[0]
    is_increasing = False
    is_decreasing = False
    for n in l[1:]:
        is_within_bounds = (1 <= abs(n - n_last) <= 3)
        if n > n_last:
            is_increasing = True
        elif n < n_last:
            is_decreasing = True
        n_last = n
        if (is_increasing and is_decreasing) or (not is_within_bounds):
            return False
    return True

print([check(l) for l in t_lists].count(True))

# part 2
def check_with_dampener(l):
    if check(l): return True
    for i in range(len(l)):
        l_ = l.copy()
        l_.pop(i)
        if check(l_): return True
    return False

print([check_with_dampener(l) for l in t_lists].count(True))

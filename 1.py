# part 1
t = open('1.txt','r').read()
t_pairs = [list(map(int,line.split())) for line in t.split('\n')][:-1]
left_list = sorted([x[0] for x in t_pairs])
right_list = sorted([x[1] for x in t_pairs])
print(sum([abs(l-r)for l,r in zip(left_list,right_list)]))
# part 2
print(sum([left_n * right_list.count(left_n) for left_n in left_list]))

# part 1
s = open('5.txt','r').read()

rules, s = s.split('\n\n')
s = [[int(n) for n in l.split(',')] for l in s.split('\n')[:-1]] 

def get_index(list_,value):
    try:
        return list_.index(value)
    except ValueError:
        return -1

def parse_rules(rules):
    rules_dict = {} 
    for l in rules.split('\n'):
        a,b = l.split('|')
        a,b = int(a),int(b)
        rules_dict.setdefault(a,[])
        rules_dict[a].append(b)
    return rules_dict

def validate_line(l,rules_dict):
    for i,n in enumerate(l):
        if n not in rules_dict.keys():
            continue
        for n_rule in rules_dict[n]:
            if get_index(l,n_rule) != -1 and i > get_index(l,n_rule):
                return False
    return True

rules_dict = parse_rules(rules)
print(sum([l[len(l)//2] for l in s if validate_line(l,rules_dict)]))

# part 2
def correct_line_once(l,rules_dict):
    l = l.copy()
    for i,n in enumerate(l):
        if n not in rules_dict.keys():
            continue
        for n_rule in rules_dict[n]:
            position = get_index(l,n_rule)
            if  position != -1 and i > position:
                l.pop(position)
                l.insert(i,n_rule)
                return l
    return l

def correct_line(l,rules_dict):
    l = l.copy()
    valid = False
    while not valid:
        valid = validate_line(l,rules_dict)
        l = correct_line_once(l,rules_dict)
    return l

invalid_lines = [l for l in s if not validate_line(l,rules_dict)]
corrected_lines = [correct_line(l,rules_dict) for l in invalid_lines]
print(sum([l[len(l)//2] for l in corrected_lines]))




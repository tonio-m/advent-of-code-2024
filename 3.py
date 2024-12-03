s = open('3.txt','r').read()

def parse_commands(s,include_do=False):
    parenthesis_open = False
    commands = []
    if include_do: do = True
    while len(s):
        if include_do: 
            if len(s) >= 4 and s[:4] == 'do()':
                s = s[4:]
                do = True
            elif len(s) >= 7 and s[:7] == "don't()":
                s = s[7:]
                do = False
        else:
            do = True

        if len(s) >= 4 and s[:4] == 'mul(' and do:
            s = s[4:]
            parenthesis_open = True
            i = 0
            n_len = 0
            while parenthesis_open:
                c = s[i]
                if c not in '0123456789,)' or n_len > 3:
                    s = s[i:]
                    parenthesis_open = False
                elif c in '0123456789':
                    n_len += 1
                elif c == ',':
                    n_len = 0
                elif c == ')':
                    parenthesis_open = False
                    command = f'mul({s[:i]})'
                    commands.append(command)
                    s = s[i:]
                i += 1
        else:
            s = s[1:]
    return commands

def eval(command):
    if command[:4] == 'mul(' and command[-1] == ')':
        a,b = command[4:-1].split(',')
        return int(a) * int(b)
    else:
        raise Exception(f'{command} this shit is malformed')

# part 1
print(sum([eval(c) for c in parse_commands(s)]))
# part 2
print(sum([eval(c) for c in parse_commands(s,include_do=True)]))

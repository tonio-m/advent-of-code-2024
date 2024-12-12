# part 1
s = open('11.txt','r').read().split()

def step(l):
    result = []
    for x in l:
        x = str(x)
        n = int(x)
        if n == 0:
            n = 1
            result.append(n)
        elif len(x) % 2 == 0:
            result.append(int(x[:len(x)//2]))
            result.append(int(x[len(x)//2:]))
        else:
            result.append(n * 2024)
    return result

for i in range(25):
    s = step(s)

print(len(s))

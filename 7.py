# part 1
import operator
import itertools

s = open('7.txt','r').read()

t = [l.split(': ') for l in s.split('\n')[:-1]]
t = [(int(total),tuple(map(int,numbers.split(' ')))) for total, numbers in t]

symbols = [operator.mul,operator.add]

def has_operators(total,numbers,symbols):
    permutations = itertools.product(symbols, repeat=(len(numbers) - 1))
    for permutation in permutations:
        result_ = numbers[0]
        for symbol_i, n in enumerate(numbers[1:]):
            result_ = permutation[symbol_i](result_,n)
            if result_ == total:
                return True
            elif result_ > total:
                break
    return False


print(sum([total for total,numbers in t if has_operators(total,numbers,symbols)]))

# part 2
def concatenation(n1,n2):
    return int(str(n1) + str(n2))

symbols = [operator.mul,operator.add,concatenation]
print(sum([total for total,numbers in t if has_operators(total,numbers,symbols)]))

# part 1
import pdb

# disk_string = '2333133121414131402'
disk_string = open('9.txt','r').read()[:-1]

def expand(digit_string):
    result = []
    is_file_digit = True
    file_id = 0
    for digit in digit_string:
        digit = int(digit)
        if is_file_digit:
            result += [str(file_id)] * digit
            file_id += 1
        else:
            result += ['.'] * digit
        is_file_digit = not is_file_digit
    return result


def last_digit(expanded_string):
    for i in range(len(expanded_string)-1,-1,-1):
        if expanded_string[i].isnumeric():
            return i
    return -1
        

def sort(expanded_string):
    queue = expanded_string.copy()
    result = []
    number_of_empty_spaces = 0
    while len(queue):
        # print(len(queue))
        # print(f'{queue=}{result=}')
        # pdb.set_trace()
        char = queue.pop(0)
        if char.isnumeric():
            result.append(char)
        elif char == '.':
            number_of_empty_spaces += 1
            last_digit_index = last_digit(queue)
            if last_digit_index == -1:
                break
            result.append(queue[last_digit_index])
            queue.pop(last_digit_index)

    return result + ['.'] * number_of_empty_spaces


def compute_checksum(sorted_):
    total = 0
    for i,x in enumerate(sorted_):
        if x == '.':
            break
        total += i*int(x)
    return total


# print(disk_string)
expanded = expand(disk_string)
# print(expanded)
sorted_ = sort(expanded)
# print(sorted_)
print(compute_checksum(sorted_))



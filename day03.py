import numpy as np
def find_duplicate(input):
    a, b = input[:len(input)//2], input[len(input)//2:]
    res = set(a) & set(b)
    return list(res)[0]

def priority(package):
    order = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    p = order.rfind(package) + 1
    return p

def process(input):
    res = find_duplicate(input)
    p = priority(res)
    return p

print("#### Test data:")
print(process('vJrwpWtwJgWrhcsFMMfFFhFp'))
print(process('jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL'))
print(process('PmmdzqPrVvPwwTWBwg'))
print(process('wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn'))
print(process('ttgJtRGJQctTZtZT'))
print(process('CrZsJsPPZsGzwwsLwLmpwMDw'))

with open('input03.txt', 'r') as fh:
    lines = fh.readlines()

total = np.array([process(line) for line in lines]).sum()
print(f"Total priority: {total}")
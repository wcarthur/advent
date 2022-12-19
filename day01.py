import numpy as np
fname = "input01.txt"

with open(fname, 'r') as fh:
    lines = fh.readlines()

values = []
tmpval = 0
for line in lines:
    if line.strip():
        tmpval += int(line)
    else:
        values.append(tmpval)
        tmpval = 0
values = np.array(values)
x = np.argmax(values) + 1
print(f"Elf #{x} carries the most ({max(values)})")


top3 = np.sum(sorted(values)[-3:])
print(f"Top 3 elves carry {top3} calories")

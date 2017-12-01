file = open("aoc1.txt")
f = file.read()
floor = 0
count = 0
for i in f:
    if i == '(':
        floor += 1
    if i == ')':
        floor -= 1
    count += 1
    if floor < 0:
        break
print("step: ", count, "floor: ", floor)

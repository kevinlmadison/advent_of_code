file = open("aoc2.txt")
dir_arr = file.readlines()
keypad = [['x', 'x', 5, 'x', 'x',], ['x', 2, 6, 'A', 'x',], [1, 3, 7, 'B', 'D'], ['x', 4, 8, 'C', 'x',], ['x', 'x', 9, 'x', 'x',]]
x = 0; y = 2
code = []
for dir_set in dir_arr:
	for dir in dir_set:
		if dir == 'U':
			if y - 1 >= 0:
				if keypad[x][y - 1] != 'x':
					y -= 1
		if dir == 'D':
			if y + 1 <= 4:
				if keypad[x][y + 1] != 'x':
					y += 1
		if dir == 'L':
			if x - 1 >= 0:
				if keypad[x - 1][y] != 'x':
					x -= 1
		if dir == 'R':
			if x + 1 <= 4:
				if keypad[x + 1][y] != 'x':
					x += 1
	code.append(keypad[x][y])
print(code)

#My ugly way of solving this problem....
file = open("aoc2.txt")
dir_arr = file.readlines()
keypad = [[1, 2, 3],[4, 5, 6],[7, 8, 9]]
x = 1; y = 1
code = []
for dir_set in dir_arr:
	for dir in dir_set:
		if dir == 'U':
			if y != 0:
				y -= 1
		if dir == 'D':
			if y != 2:
				y += 1
		if dir == 'L':
			if x != 0:
				x -= 1
		if dir == 'R':
			if x != 2:
				x += 1
	code.append(keypad[y][x])
print(code)
def is_abba(list):
	if len(list) > 0:
		for j in list:
			if len(j) > 3:
				for i in range(len(j) - 3):
					if j[i] == j[i+3] and j[i+1] == j[i+2] and j[i] != j[i+1]:
						return True
	return False
def is_aba(aba_list, bab_list):
	if len(aba_list) > 0 and len(bab_list) > 0:
		for j in aba_list:
			if len(j) > 2:
				for i in range(len(j) - 2):
					if j[i] == j[i+2] and j[i] != j[i+1]:
						for k in bab_list:
							test = j[i+1] + j[i] + j[i+1]
							if test in k:
								print(test, k)
								return True
	return False

def part1():
	file = open("aoc7.txt")
	count = 0
	for line in file:
		abba = []
		not_abba = []
		line = line.strip('\n')
		line = line.split('[')
		for i in line:
			if ']' in i:
				index = i.index(']')
				abba.append(i[index+1:])
				not_abba.append(i[:index])
			else:
				abba.append(i)
		print("abba: ", abba)
		print("not abba: ", not_abba)
		if is_abba(abba) and not is_abba(not_abba):
			count += 1
	print(count)
	
def part2():
	file = open("aoc7.txt")
	count = 0
	lines = 0
	for line in file:
		lines += 1
		aba = []
		bab = []
		line = line.strip('\n')
		line = line.split('[')
		for i in line:
			if ']' in i:
				index = i.index(']')
				aba.append(i[index+1:])
				bab.append(i[:index])
			else:
				aba.append(i)
		##################
		if is_aba(aba, bab) == True:
			count += 1
	print(count, lines)
part2()
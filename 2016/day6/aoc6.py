
def most(list):
	count = 0
	index = 0
	for i in list:
		if list.count(i) > count:
			count = list.count(i)
			index = list.index(i)
	return list[index]
	
def least(list):
	count = len(list)
	index = 0
	for i in list:
		if list.count(i) < count:
			count = list.count(i)
			index = list.index(i)
	return list[index]
file = open('aoc6.txt')
arr=[[], [], [], [], [], [], [], []]
for line in file:
	for i in range(8):
		arr[i].append(line[i])
for i in arr:
	print(most(i), least(i))

	

	
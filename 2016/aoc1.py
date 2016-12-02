
class direction:
    def __init__(self):
        self.dirs = ['n', 'e', 's', 'w']

    def __len__(self):
        return len(self.dirs)

    def __getitem__(self, i):
        return self.dirs[i]

    def turn_left(self):
        last = self.dirs.pop()
        self.dirs.insert(0, last)

    def turn_right(self):
        first = self.dirs.pop(0)
        self.dirs.append(first)

    def get_current_directin(self):
        return self.dirs[0]

    def show(self):
        print(self.dirs)

curr_dir = direction()
x = 0
y = 0
aoc = open('aoc1.txt')
aoc_list = aoc.read().split(', ')
visited = []
done = False
for i in aoc_list:
    xi = x
    yi = y
    if i[0] == 'R':
        curr_dir.turn_right()
    if i[0] == 'L':
        curr_dir.turn_left()
    if curr_dir.get_current_directin() == 'n':
        y += int(i[1:])
    if curr_dir.get_current_directin() == 'e':
        x += int(i[1:])
    if curr_dir.get_current_directin() == 's':
        y -= int(i[1:])
    if curr_dir.get_current_directin() == 'w':
        x -= int(i[1:])
    xf = []
    yf = []
    x_step = 1
    y_step = 1
    if x < xi:
        x_step = -1
    if y < yi:
        y_step = -1
    if x - xi != 0:
        for i in range(xi, x, x_step):
            xf.append(i)
            yf.append(y)
    if y - yi != 0:
        for i in range(yi, y, y_step):
            yf.append(i)
            xf.append(x)
    for i in range(len(xf)):
        print([xf[i], yf[i]])
        check = [xf[i], yf[i]]
        if check in visited and done == False:
            done = True
            print("CROSSOVER %d UNITS AWAY!!!!", (xf[i] + yf[i]))
        visited.append([xf[i], yf[i]])
print("coordinates x: %d y: %d \nyou are %d blocks away \
from your target." % (x, y, x + y))

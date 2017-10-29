#This is A* search if I'm not mistaken
def is_wall(x, y):
    q = (x*x + 3*x + 2*x*y + y + y*y) + 1352
    return bin(q).count('1') % 2 == 1

trav = {(1,1)}
steps = 0
new = trav

part1 = None
part2 = None

while part1 is None or part2 is None:
    check = new.copy()
    new = set()
    for x0, y0 in check:
        for x, y in [(x0 + 1, y0), (x0 - 1, y0), (x0, y0 + 1), (x0, y0 - 1)]:
            if x < 0 or y < 0 or (x, y) in trav or is_wall(x, y):
                continue
            trav.add((x, y))
            new.add((x, y))
    steps += 1
    if (31, 39) in new:
        part1 = steps
    if steps == 50:
        part2 = len(trav)

print(part1)
print(part2)

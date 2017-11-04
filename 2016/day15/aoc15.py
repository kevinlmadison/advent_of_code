t = 0
loop = True
slots = [5, 8, 1, 7, 1, 0, 0]

while loop:
    t += 1
    for i in range(7):
        slots[i] += 1
    if slots[0] == 17:
        slots[0] = 0
    if slots[1] == 19:
        slots[1] = 0
    if slots[2] == 7:
        slots[2] = 0
    if slots[3] == 13:
        slots[3] = 0
    if slots[4] == 5:
        slots[4] = 0
    if slots[5] == 3:
        slots[5] = 0
    if slots[6] == 11:
        slots[6] = 0

    if slots == [16, 17, 4, 9, 0, 0, 4]:
        loop = False
        print(str(t))

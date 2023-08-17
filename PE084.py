from random import randint
board = [0] * 40
cnt = 0
pos = 0
doubles = 0

while cnt < 10000000:
    d1 = randint(0, 3) + 1
    d2 = randint(0, 3) + 1
    pos += (d1 + d2)
    if d1 == d2:
        doubles += 1
    else:
        doubles = 0

    if pos > 39:
        pos -= 40
    if pos == 2 or pos == 17 or pos == 33:
        r = randint(0, 15) + 1
        if r == 1:
            pos = 0
        elif r == 2:
            pos = 10
    if pos == 7 or pos == 22 or pos == 36:
        r = randint(0, 15) + 1
        if r == 1:
            pos = 0
        elif r == 2:
            pos = 10
        elif r == 3:
            pos = 11
        elif r == 4:
            pos = 24
        elif r == 5:
            pos = 39
        elif r == 6:
            pos = 5
        if r == 7 or r == 8:
            if pos == 7:
                pos = 15
            elif pos == 22:
                pos = 25
            elif pos == 36:
                pos = 5
        if r == 9:
            if pos == 7:
                pos = 12
            elif pos == 22:
                pos = 28
            elif pos == 36:
                pos = 12
        if r == 10:
            pos -= 3
    if pos == 30 or doubles == 3:
        pos = 10
    board[pos] += 1
    cnt += 1

name = [i for i in range(40)]
for i in sorted(zip(board, name), reverse=True)[:3]:
    print(i[1], end='')

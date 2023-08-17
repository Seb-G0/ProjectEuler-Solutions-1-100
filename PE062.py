def PE062():
    n = 1
    per = dict()
    while True:
        cube = str(n ** 3)
        p = ''.join(sorted(list(cube)))
        if p in per:
            per[p][1] += 1
        else:
            per[p] = [cube, 1]
        if per[p][1] == 5:
            return per[p][0]
        n += 1

print(PE062())
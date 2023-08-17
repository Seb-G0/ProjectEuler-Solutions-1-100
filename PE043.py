ints = ['0', '1', '2', '3', '4', '5', '6', '7', '8','9']
mods = [0, 2, 3, 5, 7, 11, 13]
total = 0
def solve(n, ds):
    global total
    mod = mods[n-1]
    if mod == 0:
        for d in ints:
            if d in ds:
                continue
            total += int(''.join([d] + ds))
    else:
        for d in ints:
            if d in ds or int(d + ds[0] + ds[1]) % mod != 0:
                continue
            solve(n-1, [d] + ds)

def PE043():
    for n in range(17, 1000, 17):
        ds = [str(n // 100), str((n // 10) % 10), str(n % 10)]
        if len(set(ds)) != len(ds):
            n += 1
            continue
        solve(7, ds)
        n += 1
    return total
print(PE043())

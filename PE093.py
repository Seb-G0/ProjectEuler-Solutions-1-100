def generate_output():
    cnt = 0
    res = []
    set1 = [1, 1, 0, 0, 0]
    while set1[0] < 5:
        set1[2] += 1

        x = 3
        while x > 0:
            if set1[x] == 5:
                set1[x] = 1
                set1[x - 1] += 1
            x -= 1

        if set1[0] == 5:
            break

        op = [''] * 3
        for o in range(3):
            if set1[o] == 1:
                op[o] = '+'
            elif set1[o] == 2:
                op[o] = '-'
            elif set1[o] == 3:
                op[o] = '*'
            elif set1[o] == 4:
                op[o] = '/'
        res.append(f"a {op[0]} b {op[1]} c {op[2]} d")
        res.append(f"a {op[0]} b {op[1]} (c {op[2]} d)")
        res.append(f"a {op[0]} (b {op[1]} c) {op[2]} d")
        res.append(f"(a {op[0]} b) {op[1]} c {op[2]} d")
        res.append(f"(a {op[0]} b {op[1]} c) {op[2]} d")
        res.append(f"(a {op[0]} (b {op[1]} c)) {op[2]} d")
        res.append(f"((a {op[0]} b) {op[1]} c) {op[2]} d")
        res.append(f"a {op[0]} (b {op[1]} c {op[2]} d)")
        res.append(f"a {op[0]} ((b {op[1]} c) {op[2]} d)")
        res.append(f"a {op[0]} (b {op[1]} (c {op[2]} d))")
        res.append(f"(a {op[0]} b) {op[1]} (c {op[2]} d)")


    return res


def logestconsecutive(n):
    num = 1
    while num in n:
        num += 1
    return num
def permutations(iterable, r=None):
    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return
    indices = [i for i in range(n)]
    cycles = [i for i in range(n, n-r, -1)]
    yield tuple(pool[i] for i in indices[:r])
    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return
equations = generate_output()

d = dict()
ans = ''
mx = 0
for a in range(1, 10):
    for b in range(a, 10):
        for c in range(b, 10):
            for d in range(c, 10):
                if len(set([a, b, c, d])) != 4:
                    continue
                results = set()
                permutation = list(permutations([a, b, c, d], 4))
                for eq in equations:
                    for a1, b1, c1, d1 in permutation:
                        try:
                            value = eval(eq, {"a": a1, "b": b1, "c": c1, "d": d1})
                        except:
                            value = 0
                        if int(value) == value:
                            results.add(abs(value))
                if logestconsecutive(results) > mx:
                    mx = logestconsecutive(results)
                    ans = a * 1000 + b * 100 + c * 10 + d


print(ans)
from functools import cache
from math import isqrt

@cache
def sumofFactors(n):
    s = n
    res = 1
    for i in range(2, isqrt(n) + 1):
        curr_sum = 1
        curr_term = 1
        while n % i == 0:
            n = n / i;
            curr_term = curr_term * i;
            curr_sum += curr_term;
        res = res * curr_sum
    if n > 2:
        res = res * (1 + n)
    return res - s

def PE095(n, initial, chain = []):
    SofF = int(sumofFactors(n))
    if SofF == initial:
        return chain + [n]
    elif SofF in seen or SofF > mx or SofF < initial or SofF in chain:
        return -1
    else:
        return PE095(SofF, initial, chain + [n])

mx = 1000000
length = [0, []]
seen = set()
for n in range(2, mx, 2):
    chain = PE095(n, n)
    if chain != -1:
        if length[0] < len(chain):
            length = [len(chain), min(chain)]
    else:
        seen.add(n)
print(length[1])

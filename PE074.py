factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
seen = dict()
def factdsum(n):
    return sum(factorials[int(i)] for i in str(n))
count = 0
for n in range(1000000):
    chain = set()
    length = 0
    sstr = str(sorted(str(n)))
    if sstr in seen:
        length = seen[sstr]
    else:
        while factdsum(n) not in chain and length <= 60:
            n = factdsum(n)
            chain.add(n)
            length += 1
        seen[sstr] = length
    if length == 59:
        count += 1
print(count)


#test


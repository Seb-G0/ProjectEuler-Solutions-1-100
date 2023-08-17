from functools import reduce
def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
def isPandigital(n):
    return len(set(str(n))) == 9
def noDuplicates(n):
    return len(set(str(n))) == len(str(n))

results = set()
for i in range(1234,9877):
    if noDuplicates(i):
        factor = factors(i)
        for num in factor:
            factor1 = num
            factor2 = int(i/num)
            total = str(factor1) + str(factor2) + str(i)
            if isPandigital(total) and '0' not in str(total):
                results.add(i)
print(sum(results))
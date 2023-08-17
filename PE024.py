from itertools import permutations
results = permutations("0123456789", 10)
results = [int("".join(p)) for p in results]
print(results[999999])
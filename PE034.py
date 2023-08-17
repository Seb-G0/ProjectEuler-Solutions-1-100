def PE034():
	total = 0
	facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
	for i in range(3, 50000):
		if sum([facts[int(j)] for j in str(i)]) == i:
			total += i
	return total
print(PE034())
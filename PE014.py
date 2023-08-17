def collatzSequence(num):
    count = 1
    while num != 1:
        if num % 2 == 0:
            num = num/2
        else:
            num = 1 + num*3
        count += 1
    return count

terms = [1,1]
for i in range(1, 1000000):
    n = collatzSequence(i)
    if terms[1] < n:
        terms[1] = n
        terms[0] = i
print(terms[0])
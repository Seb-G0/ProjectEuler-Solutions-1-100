def PE052():
    n = 1
    while True:
        n2, n3, n4, n5, n6 = 2 * n, 3 * n, 4 * n, 5 * n, 6 * n
        if sorted(str(n)) == sorted(str(n2)) == sorted(str(n3)) == sorted(str(n4)) == sorted(str(n5)) == sorted(str(n6)):
            return n
        n +=1
print(PE052())
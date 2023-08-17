def PE028(t):
    n = (t-1) / 2
    return 8 * n * (n + 1) * (2 * n + 1) / 3 + 2 * n * (n+1) + 4 * n + 1
print(PE028(1001))
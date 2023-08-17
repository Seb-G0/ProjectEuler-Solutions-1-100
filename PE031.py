coins = [1, 2, 5, 10, 20, 50, 100, 200]
amount = 200
ways = [0] * (amount + 1)
ways[0] = 1
for i in range(1, 9):
    for j in range(coins[i - 1], amount + 1):
        ways[j] += ways[j - coins[i - 1]]
print(ways[amount])
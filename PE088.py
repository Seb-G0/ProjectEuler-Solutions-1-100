def get_prime_factors(n):
    factors = []
    d = 2
    while d * d <= n:
        while (n % d) == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def PE089(limit):
    min_product_sum = [2 * limit] * (limit + 1)

    def dfs(product, sum_val, factors_count, start):
        k = product - sum_val + factors_count
        if k <= limit and product < min_product_sum[k]:
            min_product_sum[k] = product
        for i in range(start, limit // product * 2 + 1):
            next_product = product * i
            next_sum = sum_val + i
            next_factors_count = factors_count + 1
            dfs(next_product, next_sum, next_factors_count, i)

    dfs(1, 1, 1, 2)
    unique_numbers = set(min_product_sum[2:])
    return sum(unique_numbers)

limit = 12000
print(PE089(limit))


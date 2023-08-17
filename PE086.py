from math import sqrt
def is_square(x):
    s = int(sqrt(x + 0.5))
    return x == s * s

def PE086():
    count = 0
    for A in range(1, 1000000):
        for S in range(2, 2 * A + 1):
            if is_square(A * A + S * S):
                count += (A + 1 - (S + 1) // 2) if S > A + 1 else S // 2
        if count >= 1000000:
            return A
print(PE086())
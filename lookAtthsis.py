def primes_sieve(limit):
    # Sieve of Eratosthenes algorithm to generate primes
    is_prime = [True] * limit
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, limit, i):
                is_prime[j] = False
    return [x for x in range(limit) if is_prime[x]]

def draw_ulam_spiral(n):
    # Pre-compute primes up to n
    primes = primes_sieve(n)

    # Create a list to store the Ulam Spiral
    spiral = []
    x, y = 0, 0
    dx, dy = 0, -1
    for i in range(1, n+1):
        if (-x/2 <= y <= x/2) and (-y/2 <= x <= y/2):
            if i in primes:
                spiral.append((x, y, "blue"))
            else:
                spiral.append((x, y, "red"))
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy
    return spiral

spiral = draw_ulam_spiral(100)
for x, y, color in spiral:
    print(f"({x}, {y}) = {color}")


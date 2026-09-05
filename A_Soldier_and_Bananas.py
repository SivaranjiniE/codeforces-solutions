def banana(n, k, w):
    s, j = 0, 0

    for i in range(1, w + 1):
        s += i * n

    j = s - k

    if j > 0:
        return j

    return 0


n, k, w = map(int, input().split())

print(banana(n, k, w))
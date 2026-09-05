def presents(n):
    arr = []

    for i in range(1, len(n) + 1):
        arr.append(n.index(i) + 1)

    return arr


size = int(input())
n = list(map(int, input().split()))

print(*presents(n))

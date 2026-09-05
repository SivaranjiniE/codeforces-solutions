def matrix():
    n = 5

    arr = []

    for i in range(n):
        row = list(map(int, input().split()))
        arr.append(row)

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                answer = abs(i - 2) + abs(j - 2)
                return answer

print(matrix())

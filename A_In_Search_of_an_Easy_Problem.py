def search(n):
    for i in range(n):
        if arr[i] == 1:
            return "HARD"

    return "EASY"


n = int(input())
arr = list(map(int, input().split()))

print(search(n))

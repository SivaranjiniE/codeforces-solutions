def maximum(n):
    count = 1
    maxi = 1

    for i in range(n - 1):
        if arr[i] < arr[i + 1]:
            count += 1
        else:
            count = 1

        maxi = max(maxi, count)

    return maxi


n = int(input())
arr = list(map(int, input().split()))

print(maximum(n))
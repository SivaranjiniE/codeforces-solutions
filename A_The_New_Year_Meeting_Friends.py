def new(arr):
    arr.sort()
    return (arr[1] - arr[0]) + (arr[2] - arr[1])


arr = list(map(int, input().split()))

print(new(arr))
def arr(n, array):
    odd = sum(num % 2 for num in array)

    if odd % 2 == 1:
        return "YES"

    if odd > 0 and odd < n:
        return "YES"

    return "NO"


t = int(input())

for i in range(t):
    n = int(input())
    array = list(map(int, input().split()))

    print(arr(n, array))
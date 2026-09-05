def apartments(n):
    digit = int(str(x)[0])
    length = len(str(x))
    result = (digit - 1) * 10
    ans = length * (length + 1) // 2
    return ans + result


n = int(input())

for i in range(n):
    x = int(input())
    print(apartments(n))
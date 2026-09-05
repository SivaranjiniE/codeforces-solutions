number,n = map(int,input().split())
last=0

for i in range(n):
    last = number % 10

    if last == 0:
        number = number // 10
    else:
        number = number - 1

print(number)
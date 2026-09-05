def bitwise():
    x = 0
    b = int(input())

    for i in range(b):
        opertion = input()

        if "++" in opertion:
            x += 1
        else:
            x -= 1

    return x

print(bitwise())
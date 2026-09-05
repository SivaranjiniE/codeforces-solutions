def chewbacca(n):
    m = ""

    while (n > 0):
        t = n % 10

        if t == 9 and n < 10:
            m += "9"

        elif (9-t) < t:
            m += str(9-t)

        else:
            m += str(t)

        n = n//10

    return m[::-1]

n = int(input())
print(chewbacca(n))
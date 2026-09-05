def fox(row):
    count = 0

    for r in range(1, row + 1):
        if r % 2 != 0:
            print("#" * col)
        else:
            count += 1

            if count % 2 != 0:
                print("." * (col - 1) + "#")
            else:
                print("#" + "." * (col - 1))


row, col = map(int, input().split())

fox(row)

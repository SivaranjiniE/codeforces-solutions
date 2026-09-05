def word_check(w):

    upper = 0
    lower = 0

    for ch in w:
        if ch.isupper():
            upper += 1
        else:
            lower += 1

    if upper > lower:
        return w.upper()
    else:
        return w.lower()

w = input()
print(word_check(w))
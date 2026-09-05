def cap(word):
    result = word[0].upper() + word[1:]
    return result

word = input()
print(cap(word))
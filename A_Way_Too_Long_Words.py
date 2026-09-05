def long_word(word):
    if len(word) > 10:
        return word[0] + str(len(word)-2) + word[-1]
    return word

n = int(input())

for _ in range(n):
    word = input()
    print(long_word(word))
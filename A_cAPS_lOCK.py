def capitial(s):
    if s.isupper() or len(s) == 1 or (s[0].islower() and s[1:].isupper()):
        print(s.swapcase())
    else:
        print(s)

s = input()
capitial(s)
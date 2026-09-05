def boy_or_girl(s):
    if len(set(s)) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"


s = input()

print(boy_or_girl(s))
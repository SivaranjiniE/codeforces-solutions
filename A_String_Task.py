s=input()
vowels="aeyiou"
ans=""
for ch in s:
    if ch.lower() in vowels:
        continue
    else:
        ans += "." + ch.lower()
print(ans)
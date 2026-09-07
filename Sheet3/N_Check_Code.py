a, b = map(int, input().split())
s = input()

if s[a] == '-':
    valid = True
    for i in range(len(s)):
        if i != a and not s[i].isdigit():
            valid = False
            break
    if valid:
        print("Yes")
    else:
        print("No")
else:
    print("No")
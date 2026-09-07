n = int(input())
a = list(map(int, input().split()))
c = 0
while True:
    e = True
    for i in range(n):
        if a[i] % 2 != 0:
            e = False
            break
    if not e:
        break
    for i in range(n):
        a[i] = a[i] // 2
    c += 1
print(c)
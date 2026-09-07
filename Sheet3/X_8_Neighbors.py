n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(input())
x, y = map(int, input().split())
x -= 1
y -= 1
ok = True
for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
        if i == x and j == y:
            continue
        if i >= 0 and i < n and j >= 0 and j < m:
            if a[i][j] != 'x':
                ok = False
if ok:
    print("yes")
else:
    print("no")
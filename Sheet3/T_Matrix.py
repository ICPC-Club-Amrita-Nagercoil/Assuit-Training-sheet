n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))
s1 = 0
s2 = 0
for i in range(n):
    s1 += a[i][i]
    s2 += a[i][n - 1 - i]
print(abs(s1 - s2))
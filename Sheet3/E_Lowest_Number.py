n = int(input())
a = list(map(int, input().split()))

lw = a[0]
pos = 0

for i in range(1, n):
    if a[i] < lw:
        lw = a[i]
        pos = i

print(lw, pos + 1)
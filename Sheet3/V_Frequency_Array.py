n, m = map(int, input().split())
a = list(map(int, input().split()))
f = [0] * (m + 1)
for i in range(n):
    f[a[i]] += 1
for i in range(1, m + 1):
    print(f[i])
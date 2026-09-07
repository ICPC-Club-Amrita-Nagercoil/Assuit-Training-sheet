t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    c = 0
    for i in range(n):
        c += 1
        for j in range(i + 1, n):
            if a[j] >= a[j - 1]:
                c += 1
            else:
                break
    print(c)
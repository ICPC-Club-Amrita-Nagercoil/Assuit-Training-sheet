t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    ans = a[0] + a[1] + 1
    for i in range(n):
        for j in range(i + 1, n):
            val = a[i] + a[j] + j - i
            if val < ans:
                ans = val
    print(ans)
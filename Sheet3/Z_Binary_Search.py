n, q = map(int, input().split())
a = list(map(int, input().split()))
a.sort()

for _ in range(q):
    x = int(input())
    l = 0
    r = n - 1
    found = False
    while l <= r:
        m = (l + r) // 2
        if a[m] == x:
            found = True
            break
        elif a[m] < x:
            l = m + 1
        else:
            r = m - 1
    if found:
        print("found")
    else:
        print("not found")
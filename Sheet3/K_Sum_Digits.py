n = int(input())
s = input()
a = []

for i in range(n):
    a.append(int(s[i]))
sum = 0
for i in range(n):
    sum += a[i]
print(sum)
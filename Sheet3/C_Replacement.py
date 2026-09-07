n = int(input())
a = list(map(int, input().split()))

for i in range(n):
    if a[i] > 0:
        a[i] = 1
    elif a[i] < 0:
        a[i] = 2

print(*a)

##(*a) is used to print the elements of the list , seperated by space rather than printing the list as a whole.

## using  print(*a) , output --> 1 2 0 1 1
## using   print(a) , output --> [1, 2, 0, 1, 1]
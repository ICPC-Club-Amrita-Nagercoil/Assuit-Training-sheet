n=int(input())
arr=list(map(int,input().split()))
mn=min(arr)
ans=arr.count(mn)
if ans%2==0:
    print("Unlucky") 
else:
    print("Lucky")
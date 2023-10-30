# cook your dish here
n = int(input())
array = list(map(int,input().split()))
total = sum(range(1,n+1))
if sum(array) == total:
    print("YES")
else:
    print("NO")

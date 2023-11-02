# cook your dish here
for _ in range(int(input())):
    n,k = map(int, input().split())
    arr = list(map(int,input().split()))
    total = 0
    for i in range(n):
        value = sum(arr[i:k+i])
        total = max(total,value)
    print(total)
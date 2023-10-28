# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    count = 0
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            temp = arr[i]
            arr[i] = arr[i+1]
            arr[i+1]= temp
            break
    if arr == sorted(arr):
        print("Yes")
    else:
        print("No")
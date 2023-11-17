# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    arr = list(map(int,input().split()))
    value = x
    max_value = x
    for i in range(len(arr)):
        value = value + arr[i]
        max_value = max(max_value, value)
        i+=1
    print(max_value)    
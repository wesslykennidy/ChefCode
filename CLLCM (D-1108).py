# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = map(int,input().split())
    odd_list = list()
    for element in arr:
        if element%2 != 0:
            odd_list.append(element)
    if len(odd_list) == n:
        print("Yes")
    else:
        print("No")
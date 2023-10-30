# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    arrayA = list(map(int,input().split()))
    max_list = list()
    for element in arrayA:
        max_return = max(abs(element-m), abs(element-1))
        max_list.append(max_return)
    print(sum(max_list))
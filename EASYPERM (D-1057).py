# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list()
    for i in range(1,n+1):
        arr.append(i)
    print(*arr[::-1])
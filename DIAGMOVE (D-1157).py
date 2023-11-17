# cook your dish here
n = int(input())
for i in range(n):
    x, y = map(int,input().split())
    if (x+y)%2 == 0:
        print("Yes")
    else:
        print("No")
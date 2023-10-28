# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    if n%2 == 0 or x%2 == 1:
        print("Yes")
    else:
        print("No")
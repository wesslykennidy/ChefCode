# cook your dish here
for _ in range(int(input())):
    a1,a2,a3,a4,a5,p = map(int,input().split())
    total_hours = (a1+a2+a3+a4+a5)*p
    if total_hours > 120:
        print("Yes")
    else:
        print("No")
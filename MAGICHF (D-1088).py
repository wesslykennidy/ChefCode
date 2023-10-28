# cook your dish here
for _ in range(int(input())):
    n,x,s = map(int,input().split())
    position = x
    for i in range(s):
        a,b = map(int,input().split())
        if position == a:
            position = b
        elif position == b:
            position = a
            
    print(position)
# cook your dish here
for _ in range(int(input())):
    n,k = map(int,input().split())
    if n == 1:
        if k == 0:
            print("No")
        else:
            print("Yes")
    
    if n > 1:
        if n%2 != 0:
            if k == 0:
                print("No")
            else:
                print("Yes")
        else:
            print("Yes")

# another renovation code 
for _ in range (int(input())):
    n, k = map(int,input().split())
    if n == 1:
        print("Yes") if k!=0 else print("No")
    else:
        print("Yes") 
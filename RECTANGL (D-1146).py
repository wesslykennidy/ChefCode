# cook your dish here
for _ in range(int(input())):
    width1, width2, length1, length2 = sorted(map(int,input().split()))
    if width1 == width2 and length1 == length2:
        print ("YES")
    else:
        print ("NO")
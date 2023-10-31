# cook your dish here
for _ in range(int(input())):
    n = int(input())
    for i in range(n):
        i,n,q = map(int,input().split())
        #if I == Q (start head, end head)
        #or (start tail, end tail)
        if i == q:
            print(n//2)
        else:
            print(n-n//2)
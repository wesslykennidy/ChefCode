# cook your dish here
for _ in range(int(input())):
    l,k = map(int,input().split())
    print("1" if l%k else "0")
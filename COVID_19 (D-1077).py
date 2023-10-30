# cook your dish here
for _ in range(int(input())):
    n,m = map(int, input().split())
    row_count, column_count = 0,0
    for i in range(0,n,2):
        row_count +=1
    for j in range(0,m,2):
        column_count +=1
    print(row_count*column_count)

#another code
for _ in range(int(input())):
    n,m = map(int,input().split())
    row_count = (n+1)//2
    column_count = (m+1)//2
    print(row_count*column_count)
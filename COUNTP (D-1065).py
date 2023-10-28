# cook your dish here
for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    even_num = 0
    odd_num = 0
    '''
    if len(A)%2 != 0:
        print("No")
    '''
    for num in A:
        if num%2 != 0:
            odd_num +=1

    if odd_num%2 == 0 and odd_num > 0:
        print("Yes")
    else:
        print("No")
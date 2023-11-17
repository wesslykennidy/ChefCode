# cook your dish here
for _ in range(int(input())):
    n, k = map(int,input().split())
    arr_list = list()
    for  i in range(n):
        t,d = map(int,input().split())
        for i in range(t):
            arr_list.append(d)
    #FIFO removal
    FIFO_removal = arr_list[k:]
    print(sum(FIFO_removal))
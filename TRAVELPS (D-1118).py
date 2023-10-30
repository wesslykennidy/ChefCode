# cook your dish here
for _ in range(int(input())):
    n,a,b = map(int,input().split())
    array = input()
    count_1 = array.count("1")
    count_0 = array.count("0")
    print(count_1*b+count_0*a)

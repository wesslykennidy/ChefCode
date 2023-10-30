# cook your dish here
for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    position = int(input())-1
    element = array[position]
    array.sort()
    for i in range(len(array)):
        if element == array[i]:
            temp = i+1
    print(temp)
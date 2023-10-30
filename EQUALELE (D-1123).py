# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    arr_dict = {}
    for element in arr:
        if element in arr_dict:
            arr_dict[element] +=1
        else:
            arr_dict[element] = 1
    
    max_frequency = max(value for value in arr_dict.values())
    print(len(arr)-max_frequency)
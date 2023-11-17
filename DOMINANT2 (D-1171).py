# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = map(int,input().split())
    arr_dict = {}
    arr_element = list()
    for element in arr:
        if element in arr_dict:
            arr_dict[element] += 1
        else:
            arr_dict[element] = 1
    max_value = max(arr_dict.values())
    
    for key, value in arr_dict.items():
        if value == max_value:
            arr_element.append(key)
    
    if len(arr_element) == 1:
        print("Yes")
    else:
        print("No")
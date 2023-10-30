# cook your dish here
for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    array_dict = {}
    for element in array:
        if element in array_dict:
            array_dict[element] += 1
        else:
            array_dict[element] = 1
    result_dict = {key:value%key for key,value in array_dict.items()}
    if all(value == 0 for value in result_dict.values()):
        print("Yes")
    else:
        print("No")
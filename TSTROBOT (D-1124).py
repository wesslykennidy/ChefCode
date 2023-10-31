# cook your dish here
for _ in range(int(input())):
    n,x = map(int,input().split())
    array = list(input())
    converted_array = [x]
    filtered_element = list()
    for element in array:
        if element == "R":
            x = x+1
            converted_array.append(x)
        else:
            x = x-1
            converted_array.append(x)
    for element in converted_array:
        if element not in filtered_element:
            filtered_element.append(element)
    print(len(filtered_element))
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    A = list(input())
    B = list(input())
    list1 = list()
    filtered_element = list()
    list1 = [B[i] for i in range(n) if A[i] != B[i]]
    for element in list1:
        if element not in filtered_element:
            filtered_element.append(element)
    print (len(filtered_element))
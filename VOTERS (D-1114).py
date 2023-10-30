# cook your dish here
n1,n2,n3 = list(map(int,input().split()))
length_array = n1+n2+n3
array_dict = {}
array_list = list()
for i in range(length_array):
    n = int(input())
    array_list.append(n)
for element in array_list:
    if element in array_dict:
        array_dict[element] +=1
    else:
        array_dict[element] = 1
        
for key,value in sorted(array_dict.items()):
    if value <= 1:
        array_dict.pop(key,value)

print(len(array_dict))
for key in sorted(array_dict):
    print(key)
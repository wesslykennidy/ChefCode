# cook your dish here
for _ in range(int(input())):
    n = int(input())
    string = input()
    string_list = list()
    
    for i in range(0,len(string),2):
        sub_string = string[i:i+2]
        if len(sub_string) == 2:
            swapped_substring = sub_string[1]+sub_string[0]
        else:
            swapped_substring = sub_string[0]
        string_list.append(swapped_substring)
    process_string = ''.join(string_list)
    
    
    transformed_dic = {'a': 'z', 'b': 'y', 'c': 'x', 'd': 'w', 'e': 'v', 'f': 'u', 'g': 't', 'h': 's', 'i': 'r',
    'j': 'q', 'k': 'p', 'l': 'o', 'm': 'n', 'n': 'm', 'o': 'l', 'p': 'k', 'q': 'j', 'r': 'i',
    's': 'h', 't': 'g', 'u': 'f', 'v': 'e', 'w': 'd', 'x': 'c', 'y': 'b', 'z': 'a'}
    transformed_string = "".join(transformed_dic.get(char,char) for char in process_string)
    print(transformed_string)
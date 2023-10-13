# cook your dish here
def count_char (n):
    if n == "AB" or n == "BA":
        return (1)
    else:
        return (0)
        
for _ in range(int(input())):
    n = input()
    converter = list()
    sister = [n[i]+n[i+1] for i in range(0,len(n),2)]
    for element in sister:
        value = count_char(element)
        converter.append(value)
    if 0 in converter:
        print("no")
    else:
        print("yes")
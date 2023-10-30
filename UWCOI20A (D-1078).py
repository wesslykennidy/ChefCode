# cook your dish here
for _ in range(int(input())):
    n = int(input())
    height_arr = list()
    for i in range(n):
        height = int(input())
        height_arr.append(height)
    print(max(height_arr))
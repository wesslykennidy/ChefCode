# cook your dish here
for _ in range(int(input())):
    point = input()
    count_1 = point.count("1")
    count_0 = point.count("0")
    if count_1 > count_0:
        print("WIN")
    else:
        print("LOSE")
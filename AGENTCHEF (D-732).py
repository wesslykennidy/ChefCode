# cook your dish here
for _ in range(int(input())):
    x = int(input())
    if (500%x != 0):
        print((500//x) + 1)
    else:
        print(500//x)
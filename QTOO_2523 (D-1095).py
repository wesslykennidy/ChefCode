# cook your dish here
for _ in range(int(input())):
    n = int(input())
    string = input()
    string_set = set(string)
    if len(string_set) < n:
        print(n-2)
    else:
        print("-1")
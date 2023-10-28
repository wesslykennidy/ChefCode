# cook your dish here
for _ in range(int(input())):
    n = int(input())
    s = input()
    r = input()
    if s.count("0") == r.count("0") and s.count("1") == r.count("1"):
        print("YES")
    else:
        print("NO")

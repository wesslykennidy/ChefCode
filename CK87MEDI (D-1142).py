# cook your dish here
import math
for _ in range(int(input())):
    n, k = map(int,input().split())
    arr = sorted(list(map(int,input().split())))
    position = math.ceil((n+k)/2)
    print(arr[position-1])
# cook your dish here
import math
for _ in range(int(input())):
    n = int(input())
    count = 0
    while n >0:
        value = math.floor(n**0.5)
        n = n-pow(value,2)
        count +=1
    print(count)
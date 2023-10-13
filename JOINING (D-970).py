# cook your dish here
import math as m
for _ in range(int(input())):
    n,k = map(int,input().split())
    print (m.ceil(n/5)- m.ceil(k/5))
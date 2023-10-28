# cook your dish here
from math import sqrt

for _ in range(int(input())):
    n,v1,v2 = map(int,input().split())
    stair_time = n*(sqrt(2))/v1
    elevator_time = n*2/v2
    if stair_time < elevator_time:
        print("Stairs")
    else:
        print("Elevator")
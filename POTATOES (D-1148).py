# cook your dish here
import math

def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(math.sqrt(n))+1):
        if n%i == 0:
            return False
    return True
    
def summation_prime(x,y):
    sum_product = x+y
    while not is_prime(sum_product):
        sum_product +=1
    return sum_product

for _ in range(int(input())):
    x,y = map(int,input().split())
    existing_farm = x+y
    z = 1
    result = summation_prime(existing_farm, z)
    print(result-existing_farm)
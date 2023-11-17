# cook your dish here
def minimum_square(n):
    max_square = n
    minimum_value = 1
    while True:
        resonance_value = minimum_value**2
        if resonance_value > n:
            return (minimum_value-1)
        minimum_value +=1
        
for _ in range(int(input())):
    n,a = map(int,input().split())
    value = minimum_square(n)
    print(value*a)
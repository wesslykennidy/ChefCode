# cook your dish here
def prize(n):
    if n >= 42:
        return (C)
    elif n >= 21:
        return (B)
    elif n>= 10:
        return (A)
    else:
        return "0"
        
for _ in range(int(input())):
    D,d,A,B,C = map(int,input().split())
    distanceCovered = D*d
    print (prize(distanceCovered))
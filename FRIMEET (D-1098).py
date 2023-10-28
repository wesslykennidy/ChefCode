# cook your dish here
def catchup (x1,x2):
    if x1 == x2:
        return True
    elif x1 > x2:
        return False
    else:
        i = 0
        while x1 <= x2:
            x1 +=i
            x2 +=2*i
            i+=1
            
        return False
        
for _ in range(int(input())):
    value1, value2 = map(int,input().split())
    if catchup(value1, value2):
        print("Yes")
    else:
        print("No")
# cook your dish here
for _ in range(int(input())):
    r1,w1,c1 = map(int,input().split())
    r2,w2,c2 = map(int,input().split())
    count1, count2 = 0,0
    if r1 > r2:
        count1 +=1
    else: count2 +=1
    if w1 > w2:
        count1 +=1
    else: count2 +=1
    if c1 > c2:
        count1 +=1
    else: count2 +=1
    
    if count1 > count2:
        print("A")
    else:
        print ("B")
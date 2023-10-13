# cook your dish here
for _ in range(int(input())):
    n = int(input())
    aliceArr = sorted(list((map(int,input().split()))))
    bobArr = sorted(list((map(int,input().split()))))
    aliceArr.pop(n-1)
    bobArr.pop(n-1)
    if sum(aliceArr) < sum(bobArr):
        print ("Alice")
    elif sum(aliceArr) > sum(bobArr):
        print ("Bob")
    else:
        print ("Draw")
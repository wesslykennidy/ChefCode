# cook your dish here
for _ in range(int(input())):
    p1,p2, k = map(int,input().split())
    #total point divided by k since k is multiplier for win round
    total_round = (p1+p2)//k
    if total_round%2 == 0:
        print("CHEF")
    else:
        print("COOK")
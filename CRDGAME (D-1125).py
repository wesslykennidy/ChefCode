# cook your dish here
for _ in range(int(input())):
    n = int(input())
    roundChef, roundMorty = 0,0
    for i in range(n):
        a,b = map(str,input().split())
        seperate_a = [int(digit) for digit in a]
        seperate_b = [int(digit) for digit in b]
        if sum(seperate_a) > sum(seperate_b):
            roundChef +=1
        elif sum(seperate_a) < sum(seperate_b):
            roundMorty +=1
        else:
            #"If both players have equal number of points then the game ends in a draw."
            roundChef +=1
            roundMorty +=1
    if roundChef > roundMorty:
        print("0", roundChef)
    elif roundChef < roundMorty:
        print("1", roundMorty)
    else:
        print("2", roundChef)
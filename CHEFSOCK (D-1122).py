# cook your dish here
jacketCost, sockCost, money = map(int,input().split())
balanceSock = money - jacketCost
if (balanceSock//sockCost)%2 == 0:
    print("Lucky Chef")
else:
    print("Unlucky Chef")
# cook your dish here
for _ in range(int(input())):
    people, unitMoney = map(int,input().split())
    peopleList = list(map(int,input().split()))
    withdrawList = list()
    for person in peopleList:
        if person <= unitMoney:
            withdrawList.append("1")
            unitMoney -= person
        else:
            withdrawList.append("0")
    print(''.join(withdrawList))
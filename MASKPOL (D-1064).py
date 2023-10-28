# cook your dish here
for _ in range(int(input())):
    totalPerson, infectedPerson = map(int,input().split())
    uninfectedPerson = totalPerson - infectedPerson
    print(min(infectedPerson, uninfectedPerson))
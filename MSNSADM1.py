'''
A football competition has just finished. The players have been given points for scoring goals and points for committing fouls. 
Now, it is up to Alex to find the best player in the tournament. 
As a programmer, your job is to help Alex by telling him the highest number of points achieved by some player.

You are given two sequences A(1),...,A(n) and B(1),...,B(n). For each valid i, player i scored A(i) goals and committed B(i) fouls.
For each goal, the player that scored it gets 20 points, and for each foul,10 points are deducted from the player that committed it.
However, if the resulting number of points of some player is negative, this player will be considered to have 0 points instead.

You need to calculate the total number of points gained by each player and tell Alex the maximum of these values.
'''


# cook your dish here
for _ in range(int(input())):
    n = int(input())
    goals = list(map(int,input().split()))
    penalties = list(map(int,input().split()))
    goals_point = list()
    penalties_point = list()
    total = list()
    for goal in goals:
        goals_point.append(goal*20)
    for penalty in penalties:
        penalties_point.append(penalty*10)
    for x,y in zip(goals_point,penalties_point):
        total.append(x-y)
    print(max(total) if max(total)>0 else "0")
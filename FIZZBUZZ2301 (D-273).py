# cook your dish here
dhoni_vote, rohit_vote, kohli_vote = map(int,input().split())
if dhoni_vote == max(dhoni_vote,rohit_vote,kohli_vote):
    print("Yes")
else:
    print("No")
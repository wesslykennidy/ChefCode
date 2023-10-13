# cook your dish here
def element (n):
    if n == "AA":
        return ("A")
    elif n == "BB":
        return ("B")
    else:
        return (0)
        
for _ in range(int(input())):
    n = int(input())
    scoreList = list()
    score = "A"+input()
    for i in range(0,len(score)-1):
        scoreElement = score[i]+score[i+1]
        scoreList.append(scoreElement)
    
    valueList = list()
    for i in scoreList:
        valueList.append(element(i))
    print (valueList.count("A"), valueList.count("B"))

# cook your dish here
for _ in range(int(input())):
    correctAnswer = sorted(list(map(int,input().split())))
    heroAnswer = sorted(list(map(int,input().split())))
    if correctAnswer == heroAnswer:
        print ("Pass")
    else:
        print ("Fail")
    
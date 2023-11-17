# cook your dish here
for _ in range(int(input())):
    assignment, minutes_taken, days_taken = map(int,input().split())
    total_minutes_taken = assignment*minutes_taken
    total_minutes = days_taken*24*60
    if total_minutes_taken <= total_minutes:
        print ("Yes")
    else:
        print("No")
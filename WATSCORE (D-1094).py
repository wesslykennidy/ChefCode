# cook your dish here
from collections import defaultdict
for _ in range(int(input())):
    n = int(input())
    max_score = defaultdict(int)
    total = 0
    for i in range (n):
        key, value = map(int,input().split())
        max_score[key] = max(max_score[key], value)
    for key, value in max_score.items():
        if key < 9:
            total += value
    print(total)
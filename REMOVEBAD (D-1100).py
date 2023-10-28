# cook your dish here
from collections import Counter

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    counter = Counter(arr)
    max_frequency = max(counter.values())
    print(n-max_frequency)
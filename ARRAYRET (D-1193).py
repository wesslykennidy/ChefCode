# cook your dish here
for _ in range(int(input())):
    n = int(input())
    array = list(map(int,input().split()))
    missing_array = list()
    total_array = sum(array)
    # example no 3, sum of array is 55, and sum of answer is 11. the coefficient is 55/11 equal to 5. 
    # since the length of array, n is 4. thus I can conclude that it will divided by (n+1)
    coefficient = total_array//(n+1)
    for element in array:
        value = element-coefficient
        missing_array.append(value)
    print(*missing_array)
# cook your dish here
for _ in range(int(input())):
    n = input()
    digit = [int(char) for char in n if char.isdigit()]
    print(sum(digit))
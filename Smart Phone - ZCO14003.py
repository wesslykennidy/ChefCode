'''
Zonal Computing Olympiad 2014, 30 Nov 2013
'''

# cook your dish here
N = int(input())
customerBudget = list()
reversedCustomer = list(i for i in range(N,0,-1))
potentialRevenue = list()
for i in range(N):
    customerBudget.append(int(input()))
customerBudget.sort()

for i in range(len(reversedCustomer)):
    potentialRevenue.append(customerBudget[i] * reversedCustomer[i])
print (max(potentialRevenue))
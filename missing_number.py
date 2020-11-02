#https://cses.fi/problemset/task/1083
n = int(input())
num = list(map(int, input().split()))
newNum = 0
for i in range(1,n):
    newNum += i
print(newNum - (sum(num)-n))
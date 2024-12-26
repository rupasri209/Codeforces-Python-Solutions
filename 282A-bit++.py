"""
PROBLEM LINK: https://codeforces.com/contest/282/problem/A
"""
num = int(input())
result = 0
for i in range(num):
    op = str(input())
    if(op == "++X" or op == "X++"):
        result += 1
    elif(op == "--X" or op == "X--"):
        result -= 1
print(result)
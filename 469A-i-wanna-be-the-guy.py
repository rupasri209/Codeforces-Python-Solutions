"""
PROBLEM LINK: https://codeforces.com/problemset/problem/469/A
"""
def ifPass(x, y):
    combined = set()
    for i in range(1,len(x)):
        combined.add(x[i])
    for i in range(1,len(y)):
        combined.add(y[i])
    return len(combined)

n = int(input())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
if (ifPass(x, y) == n):
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
"""
PROBLEM LINK: https://codeforces.com/problemset/problem/617/A
"""
def minSteps(num):
    if num <=0:
        return 0
    i = 5
    steps = 0
    while (num > 0):
        steps = steps + num // i
        num = num - (num//i)*i
        i -= 1
    return steps

num = int(input())
print(minSteps(num))
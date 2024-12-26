"""
PROBLEM LINK: https://codeforces.com/contest/318/problem/A
"""
import math
n,k = list(map(int,input().split()))

mid = math.ceil(n/2)

if k > mid:
    print(2*(k-mid))
else:
    print(2*k-1)
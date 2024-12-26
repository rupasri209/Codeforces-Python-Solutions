"""
PROBLEM LINK: https://codeforces.com/contest/279/problem/B
"""
input1 = list(map(int, input().split()))
books, time = input1[0], input1[1]
times = list(map(int, input().split()))
sumtime , count, j = 0, 0, 0
for i in range(books):
    sumtime += times[i];
    if(sumtime <= time):
        count += 1
    else:
        sumtime -= times[j];
        j += 1
print(count)

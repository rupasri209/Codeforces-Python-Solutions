"""
PROBLEM LINK: https://codeforces.com/contest/110/problem/A
"""
num = input()
count = 0
for i in num:
    if i == "4" or i == "7":
        count += 1
count = str(count)
status = "YES"
for i in count:
    if i != "4" and i != "7":
        status = "NO"
print(status)
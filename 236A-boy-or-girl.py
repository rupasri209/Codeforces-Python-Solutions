"""
PROBLEM LINK: https://codeforces.com/contest/236/problem/A
"""
user_name = input()
letters = {}
for i in user_name:
    if i not in letters:
        letters[i] = i
if(len(letters) % 2 == 0):
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
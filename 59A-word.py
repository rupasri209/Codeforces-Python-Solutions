"""
PROBLEM LINK: https://codeforces.com/problemset/problem/59/A
"""
word = input()
count_uppercase, count_lowercase = 0,0
for char in word:
    if char.isupper():
        count_uppercase += 1
    else:
        count_lowercase += 1

if count_uppercase > count_lowercase:
    print(word.upper())
else:
    print(word.lower())
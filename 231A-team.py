"""
PROBLEM LINK: https://codeforces.com/contest/231/problem/A
"""
#SOLUTION 1
num = int(input())
solve = 0
problems = []
for i in range(num):
    problem = list(map(int,input().split()))
    problems.append(problem)
for i in range(num):
    count = 0
    for j in range(3):
        if problems[i][j] == 1:
            count += 1
    if(count >= 2):
        solve += 1
print(solve)


# SOLUTION 2
num = int(input())
solve = 0
problems = []
for i in range(num):
    problem = list(map(int,input().split()))
    petya, vasya, tonya = problem[0], problem[1], problem[2]
    solvable = petya + vasya + tonya
    if(solvable >= 2):
        solve += 1
print(solve)
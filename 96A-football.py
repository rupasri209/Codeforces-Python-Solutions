"""
PROBLEM LINK: https://codeforces.com/contest/96/problem/A
"""
position = input()
def isDangerous(position):
    if(len(position) < 7):
        return "NO"
    for i in range(len(position)-6):
        sub_position = position[i: i+7]
        if(sub_position == "0000000" or sub_position == "1111111"):
            return "YES"
    return "NO"
print(isDangerous(position))

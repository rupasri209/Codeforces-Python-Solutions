"""
PROBLEM LINK: https://codeforces.com/problemset/problem/32/B
"""
def decode(borze_code):
    length = len(borze_code)
    idx, number = 0, ""
    while(idx < length):
        if (borze_code[idx] == '-'):
            if(borze_code[idx + 1] == '-'):
                number += '2'
            else:
                number += '1'
            idx += 2
        else:
            number += '0'
            idx += 1
    return number
borze_code = input()
print(decode(borze_code))
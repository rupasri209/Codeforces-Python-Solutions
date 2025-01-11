"""
PROBLEM LINK: https://codeforces.com/problemset/problem/160/A
"""
def numOfCoins(coins):
    coins.sort()
    total_amount, current_amount, coins_count = 0, 0, 0
    for coin in coins:
        total_amount += coin

    for i in range(len(coins)-1,-1,-1):
        if current_amount > (total_amount - current_amount):
            return coins_count
        current_amount += coins[i]
        coins_count += 1
    return coins_count

num = int(input())
coins = list(map(int, input().split()))
print(numOfCoins(coins))


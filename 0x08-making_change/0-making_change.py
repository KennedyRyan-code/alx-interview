#!/usr/bin/python3
"""
Module for making change with coins
"""


def makeChange(coins, total):
    """
    Determines the fewest number of coins needed to meet a given amount total.
    Args:
        coins (list): list of coin denomiinations available.
        total (int): Total amount to make change for.
    Return:
        int: Fewest number of coins needed to meet total.
            Return -1 if total cannot be met by any number of coins.
    """
    if total < 0:
        return -1

    # Initialize a list to store minimum number of coins needed for each total
    # from 0 to total
    min_coins = [float('inf')] * (total + 1)
    min_coins[0] = 0

    # Compute minimum coins for each total from 1 to total
    for t in range(1, total + 1):
        for coin in coins:
            if t - coin >= 0:
                min_coins[t] = min(min_coins[t], min_coins[t - coin] + 1)

    return min_coins[total] if min_coins[total] != float('inf') else -1

#! /usr/bin/env python3
"""
coins.py --- starter file for CSC 321: homework 4

This program reads a set of coins from standard input,
then prints the results of making change using both
a greedy algorithm and an optimal algorithm.

You need to modify this program to implement a dynamic
programming algorithm for making optimal change.

Example Usage: ./coins.py < coins1.txt
"""

import sys


def greedy(coins, value):
    """Determines the number of coins the greedy algorithm uses
    to make change for value."""
    change = [0 for c in coins]
    for c in sorted(coins, reverse=True):
        change[coins.index(c)] = value // c
        value %= c
    return change


def coinChange(self, coins, amount):
    """
    :type coins: List[int]
    :type amount: int
    :rtype: int
    """
    n = amount
    minCoins = n  # this is because worst case is n coins of value 1
    currentMin = 0
    coinSet = {1}

    for coin in coins:
        coinSet.add(coin)

    opt = [0] * (n + 1)  # array full of zeroes
    opt[1] = 1  # problem of size 1 is best filled by single penny

    for i in range(n + 1):
        currMin = 10000
        if i in coinSet:
            opt[i] = 1
        else:
            # check if coinsSet contains value
            # double for loop from j up to i with j checking opt array and i checking for coin denominations
            for j in range(i):
                temp = opt[j] + opt[i - j]
                if temp < currMin:
                    currMin = temp
            opt[i] = currMin
    return opt[n]


def read_input():
    data = sys.stdin.read().split("\n")
    coins = sorted([int(c) for c in data[0].strip().split()])
    values = [int(c) for c in data[1].strip().split()]
    return coins, values


def main():
    coins, values = read_input()
    header = "amount algorithm | " + " ".join([str(c).ljust(4) for c in coins])
    print(header)
    print("-" * len(header))
    for v in values:
        g = greedy(coins, v)
        d = dynamic(coins, v)
        print(str(v).ljust(7) + "greedy    | " + " ".join([str(c).ljust(4) for c in g]))
        print(str(v).ljust(7) + "dynamic   | " + " ".join([str(c).ljust(4) for c in d]))


if __name__ == "__main__":
    main()
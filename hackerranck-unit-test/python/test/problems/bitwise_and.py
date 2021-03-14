"""
    Autor: <Dante Fana Badia>dfana@dfb.com.do
    Ref: https://www.hackerrank.com/challenges/30-bitwise-and/problem
"""


def bitwise_and(n, k):
    if ((k-1) | k) <= n:
        return k-1
    else:
        return k-2

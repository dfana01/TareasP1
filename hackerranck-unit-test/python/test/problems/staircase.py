"""
    Autor: <Dante Fana Badia>dfana@dfb.com.do
    Ref: https://www.hackerrank.com/challenges/staircase/problem
"""


def staircase(n):
    out = ""
    for i in range(0, n):
        out += " "*(n-(i+1)) + "#"*(i+1) + "\n"
    return out


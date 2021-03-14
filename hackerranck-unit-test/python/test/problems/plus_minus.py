"""
    Autor: <Dante Fana Badia>dfana@dfb.com.do
    Ref: https://www.hackerrank.com/challenges/plus-minus/problem
"""


def plus_minus(arr):
    proportions = [0] * 3
    for x in arr:
        if x == 0:
            proportions[0] += 1
        elif x < 0:
            proportions[1] += 1
        elif x > 0:
            proportions[2] += 1
    total = len(arr)
    return round(proportions[2]/total, 6), round(proportions[1]/total, 6), round(proportions[0]/total, 6)

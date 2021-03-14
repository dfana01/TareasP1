"""
    Autor: <Dante Fana Badia>dfana@dfb.com.do
    Ref: https://www.hackerrank.com/challenges/30-nested-logic/problem
"""


def nested_logic(dmy, dmy1):
    rd, rm, ry = [int(x) for x in dmy.split(' ')]
    ed, em, ey = [int(x) for x in dmy1.split(' ')]
    if (ry, rm, rd) <= (ey, em, ed):
        return 0
    elif (ry, rm) == (ey, em):
        return 15 * (rd - ed)
    elif ry == ey:
        return 500 * (rm - em)
    else:
        return 10000

"""
    Autor: <Dante Fana Badia>dfana@dfb.com.do
    Ref: https://www.hackerrank.com/challenges/poisonous-plants
"""


def poisonous_plants(p):
    stack = []
    max_day = 0
    for plant in p:
        day = 0
        while stack and stack[-1][0] >= plant:
            day = max(day, stack.pop()[1])

        if stack:
            day += 1
        else:
            day = 0

        max_day = max(max_day, day)
        stack.append([plant, day])

    return max_day

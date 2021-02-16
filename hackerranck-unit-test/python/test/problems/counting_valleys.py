"""
    Autor: <Dante Fana Badia>dfana@dfb.com.do
    Ref: https://www.hackerrank.com/challenges/counting-valleys/problem
"""


def counting_valleys(steps, path):
    position = 0
    valleys = 0
    for step in path:
        if step == 'U':
            position += 1
        elif step == 'D':
            position -= 1
        if position == 0 and step == 'U':
            valleys += 1
    return valleys


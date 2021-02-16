"""
    Autor: <Dante Fana Badia>dfana@dfb.com.do
    Ref: https://www.hackerrank.com/challenges/new-year-chaos
"""


def minimum_bribes(q):
    swap = 0
    for i in range(len(q)-1, 0, -1):
        if q[i] != i+1:
            if q[i-1] == i+1:
                swap += 1
                q[i-1], q[i] = q[i], q[i-1]
            elif q[i-2] == i+1:
                swap += 2
                q[i-2], q[i-1], q[i] = q[i-1], q[i], q[i-2]
            else:
                return "Too chaotic"
    return swap

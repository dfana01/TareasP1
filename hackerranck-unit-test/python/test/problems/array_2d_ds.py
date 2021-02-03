"""
    Autor: <Dante Fana Badia>dfana@dfb.com.do
    Ref: https://www.hackerrank.com/challenges/2d-array/problem
"""


def hourglassSum(arr):
    n = len(arr)
    r = -99999
    for i in range(0, n - 1):
        for j in range(0, n - 1):
            if j != 0 and i != 0 and i != n - 1 and j != n - 1:
                aux_sum = sum(
                    (arr[i-1][j-1], arr[i-1][j], arr[i-1][j+1], arr[i][j], arr[i+1][j-1], arr[i+1][j], arr[i+1][j+1])
                )
                r = r if r > aux_sum else aux_sum
    return r


if __name__ == '__main__':
    arr = []
    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    result = hourglassSum(arr)
    print(result)


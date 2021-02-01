"""
minDist = infinity
for i = 1 to length(P) - 1 do
    for j = i + 1 to length(P) do
        let p = P[i], q = P[j]
        if dist(p, q) < minDist then
            minDist = dist(p, q)
            closestPair = (p, q)
return closestPair
"""


def save_c(dic, key):
    if key in dic:
        dic[key] += 1
    else:
        dic[key] = 1


def calculate_close_pair(arr):
    dic = {}
    save_c(dic, 'c1')
    close_pair, min_dist = (), float('inf')
    save_c(dic, 'c2')
    for i in range(1, len(arr) - 1):
        save_c(dic, 'c3')
        for j in range(i + 1, len(arr)):
            save_c(dic, 'c4')
            p, q = arr[i], arr[j]
            save_c(dic, 'c5')
            if (p - q) < min_dist:
                save_c(dic, 'c6')
                min_dist = p - q
                save_c(dic, 'c7')
                close_pair = (p, q)
    save_c(dic, 'c8')
    print(dic)
    return close_pair


"""
function LevenshteinDistance(chat s[1..m], char t[1..n]):
    declare int d[0..m, 0..n]
    set each element in d to zero

    for i from 1 to m:
        d[i, 0] := i

    for j from 1 to n:
        d[0, j] := j

    for j from 1 to n:
        for i from 1 to m:
            if s[i] - t[j]:
                substitutionCost := 0
            else:
                substitutionCost := 1

            d[i, j] := minimun(d[i-1, j] + 1,
                            d[i, j-1] + 1,
                            d[i-1, j-1] + substitutionCost)
    return d[m, n]
"""


def levenshtein_distance(s1, s2):
    dic = {}
    m, n = len(s1), len(s2)

    save_c(dic, 'C1')
    d = [[0 for _ in range(n)] for _ in range(m)]

    save_c(dic, 'C2')
    for i in range(1, m):
        save_c(dic, 'C3')
        d[i][0] = i

    save_c(dic, 'C4')
    for j in range(1, n):
        save_c(dic, 'C5')
        d[0][j] = j

    save_c(dic, 'C6')
    for j in range(1, n):
        save_c(dic, 'C7')
        for i in range(1, m):
            save_c(dic, 'C8')
            save_c(dic, 'C9')
            substitution_cost = 0
            if len(s2[j]) - len(s1[i]):
                save_c(dic, 'C10')
                substitution_cost = 0
                save_c(dic, 'C11')
            else:
                save_c(dic, 'C12')
                substitution_cost = 1
            save_c(dic, 'C13')
            d[i][j] = min([
                d[i - 1][j] + 1,
                d[i][j - 1] + 1,
                d[i - 1][j - 1] + substitution_cost
            ])
    save_c(dic, 'C14')
    print(dic)
    return d[m-1][n-1]


if __name__ == '__main__':
    LIST_TEST = [82, 69, 7, 31, 57]
    values = LIST_TEST
    print("closestPair")
    print("N = {}".format(len(values)))
    print(calculate_close_pair(values))

    N = "abc"
    M = "abcasdf"
    print("levenshteinDistance")
    print("M = {}, N = {}".format(len(N), len(M)))
    print(levenshtein_distance(N, M))

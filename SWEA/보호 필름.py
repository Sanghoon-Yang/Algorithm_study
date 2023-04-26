def testPerformance(A):  # 필름 성능 검사
    for c in range(W):
        cnt = 1
        for r in range(1, D):
            if A[r][c] == A[r - 1][c]:
                cnt += 1
            else:
                cnt = 1
            if cnt >= K:
                break
        if cnt < K:
            return False
    return True


def comb(depth, idx, pick):
    global result
    if depth >= result:
        return

    if depth == pick:
        if testPerformance(film):
            result = min(result, depth)
        return

    for i in range(idx, D):
        for d in range(2):
            film[i] = drugs[d]
            comb(depth + 1, i + 1, pick)
            film[i] = raw[i]


# main
T = int(input())
for test in range(T):
    D, W, K = map(int, input().split())
    film = [list(map(int, input().split())) for _ in range(D)]
    raw = [f[:] for f in film]
    drugs = [[0] * W, [1] * W]

    if testPerformance(film):
        result = 0
    else:
        result = 1e9
        for pick in range(1, D + 1):
            comb(0, 0, pick)


    print("#{} {}".format(test + 1, result))
def check_route(route):
    ramp = [0]*n
    for i in range(n-1):
        if abs(route[i] - route[i+1]) > 1:
            return False
        else:
            if route[i] - route[i+1] == 1:
                if i + 1 + l > n:
                    return False
                for j in range(i+1,i+l+1):
                    if ramp[j] or route[j] != route[i+1]:
                        return False
                    ramp[j] = 1
            elif route[i] - route[i+1] == -1:
                if i+1-l < 0:
                    return False
                for j in range(i, i-l, -1):
                    if ramp[j] or route[j] != route[i]:
                        return False
                    ramp[j] = 1
    return True





if __name__=='__main__':
    n, l = map(int, input().split())

    a = [list(map(int, input().split())) for _ in range(n)]

    # row check
    cnt = 0
    for r in a:
        if check_route(r):
            cnt += 1

    for c in range(n):
            if check_route([a[r][c] for r in range(n)]):
                cnt += 1
    print(cnt-1)





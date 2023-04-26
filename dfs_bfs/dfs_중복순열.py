def permutation(l):
    if l == m:
        for j in range(m):
            print(res[j], end=" ")
        print()
    else:
        for i in range(1, n+1):
            res[l] = i
            permutation(l+1)




if __name__=='__main__':
    n,m = map(int, input().split())
    res = [0]*m
    permutation(0)
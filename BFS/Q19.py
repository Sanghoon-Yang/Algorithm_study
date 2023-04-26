n = int(input())
a = list(map(int, input().split()))
plus, minus, mult, div = map(int, input().split())
min_val = -1e9
max_val = 1e9
def dfs(i, now):
    global min_val, max_val, plus, minus, mult, div
    if i == n:
        print(max(max_val, now))
        print(min(min_val, now))





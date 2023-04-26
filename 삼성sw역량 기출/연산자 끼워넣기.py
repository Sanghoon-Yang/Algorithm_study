import sys
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))
cal = list(map(int, input().split()))

minimum = 1e9
maximum = -1e9

def dfs(depth, total, plus, minus, mult, div):
    global minimum, maximum

    if depth == n:
        maximum = (max(total, maximum))
        minimum = (min(total, minimum))
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus-1, minus, mult, div)
    if minus:
        dfs(depth + 1, total - num[depth], plus , minus-1, mult, div)
    if mult:
        dfs(depth + 1, total * num[depth], plus, minus, mult-1, div)
    if div:
        dfs(depth + 1, int(total / num[depth]), plus, minus, mult, div-1)


dfs(1, num[0], cal[0], cal[1], cal[2], cal[3])

print(maximum)
print(minimum)
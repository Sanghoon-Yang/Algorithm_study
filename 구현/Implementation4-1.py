n = int(input())
path = list(input().split())



def path_finding(start, path):
    for i in path:
        print(i)
        if i == 'R':
            start[1] += 1
            if start[0] < 1 or start[1] < 1 or start[0] > n or start[1] > n:
                start[1] -= 1
                continue
        elif i == 'L':
            start[1] -= 1
            if start[0] < 1 or start[1] < 1 or start[0] > n or start[1] > n:
                start[1] += 1
                continue
        elif i == 'U':
            start[0] -= 1
            if start[0] < 1 or start[1] < 1 or start[0] > n or start[1] > n:
                start[0] += 1
                continue
        elif i == 'D':
            start[0] += 1
            if start[0] < 1 or start[1] < 1 or start[0] > n or start[1] > n:
                start[0] -= 1
                continue
        print(start)
    return start

start = [1, 1]
start = path_finding(start, path)

print(start)
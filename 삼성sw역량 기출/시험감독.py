n = int(input())
people = list(map(int, input().split()))
b ,c = map(int, input().split())
cnt = n

for i in people:
    if i >= b:
        i -= b
        if i % c == 0:
            cnt += i//c
        else:
            cnt += i//c +1

print(cnt)

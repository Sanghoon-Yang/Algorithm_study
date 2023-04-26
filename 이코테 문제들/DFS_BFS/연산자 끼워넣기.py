#N개로 이루어진 수열 A1234~N까지 주어짐
#수와 수 사이에 끼워넣을 수 있는 N-1개의 연산자가 주어짐
#연산자는 + - X / 으로 주어짐
#나눗셈은 정수 나눗셈으로 몫만 취하기
#음수를 양수로 나눌 때는 양수로 바꾼 뒤, 몫을 취하고 그 몫을 음수로 바꿈

n = int(input())
number = list(map(int, input().split()))

max_val = -1e09
min_val = 1e09
# + - X / 개수
plus, minus, multi, divide = map(int, input().split())

def dfs(i,now):
    global min_val, max_val,plus,minus,multi,divide

    if i == n:
        min_val = min(min_val, now)
        max_val = max(max_val, now)

    else:
        if plus > 0:
            plus -= 1
            dfs(i+1, now + number[i])
            plus += 1
        if minus > 0:
            minus -= 1
            dfs(i+1, now - number[i])
            minus += 1
        if multi > 0:
            multi -= 1
            dfs(i+1, now * number[i])
            multi += 1
        if divide > 0:
            divide -= 1
            dfs(i+1, int(now / number[i]))
            divide += 1

dfs(1, number[0])

print(max_val)
print(min_val)
#N이 1이 될 때 까지 다음이 두 과정중 하나를 반복적으로 선택하여 수행
# 1. N에서 1을 뺀다
# 2. N을 K로 나눈다

N, K = map(int, input().split())

answer = 0

while N > 1:

    if N % K == 0:
        N /= K
        answer += 1
        if N == 1:
            break

    else:
        N -= 1
        answer += 1
        if N == 1:
            break




print(answer)
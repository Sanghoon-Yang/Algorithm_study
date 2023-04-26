#다양한 수로 이루어진 배열이 있을 때 주어진 수들을 M번 더하여 가장 큰 수를 만드는 법칙
#배열의 특정한 인덱스에 해당하나는 수가 연속해서 K번 초과하여 더해질 수 없는 것이 법칙의 특성

N,M,K = map(int, input().split())
N_list = list(map(int, input().split()))

N_list = sorted(N_list, reverse=True)
first, second = N_list[0], N_list[1]
answer = 0
check = 0
for m in range(M):

    if check == K:
        answer += second
        check = 0
    else:
        answer += first
    check += 1

print(answer)
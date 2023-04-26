#숫자가 쓰인 카드들이 N X M의 형태로 N은 행
#먼저 뽑고자 하는 카드가 포함되어있는 행 선택
#선탣ㄱ된 행에 포함된 카드들 중 가장 숫자가 낮은 카드를 뽑
N,M = map(int, input().split())
card = []
for _ in range(N):
    card.append(list(map(int, input().split())))
answer = 0
for n in range(N):
    answer = max(min(card[n]), answer)

print(answer)
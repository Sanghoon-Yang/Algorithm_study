#각자리 숫자 (0~9) 로만 이루어진 문자열 S
#왼쪽부터 오른쪽으로 숫자 사이에 X 혹은 + 를 넣어 결과적으로 가장 큰수를 구하는 프로그램 작성하기.

#뒤에 0이 나온다면 곱하지 말고 더해야함

S = input()
answer = 0
for s in S:
    s = int(s)
    if s == 0 or answer == 0:
        answer += s
    else:
        answer *= s
print(answer)
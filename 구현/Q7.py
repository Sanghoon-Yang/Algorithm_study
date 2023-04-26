score = input()
leng = len(score)
half = int(leng/2)

half1 = score[0:half]
half2 = score[half:leng]

count1 = 0
count2 = 0

for i in half1:
    count1 += int(i)
for j in half2:
    count2 += int(j)

if count1 == count2:
    print('LUCKY')
else:
    print('READY')
M = 3
my_list = [1,2,3,4]
choosen_result = []

def combination(depth, idx):
    if depth == M:
        print(choosen_result)
        return

    for i in range(idx, len(my_list)):
        if my_list[i] in choosen_result:
            continue
        choosen_result.append(my_list[i])
        combination(depth +1, i+1)
        choosen_result.pop()



combination(0,0)
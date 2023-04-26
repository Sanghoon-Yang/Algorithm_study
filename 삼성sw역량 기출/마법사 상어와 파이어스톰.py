n,q = map(int, input().split())
mapp =[]

for _ in range(2**n):
    mapp.append(list(map(int, input().split())))

l_list = list(map(int, input().split()))
print(len(mapp))
def rot_90(arr):
    new_arr = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            new_arr[i][j] = arr[j][len(arr) - i]

    return new_arr


#
# for fire_storm in range(q):
#     l = l_list[fire_storm]
#
arr = [[0,1,2,3],[1,2,3,4],[4,5,6,7],[1,3,5,7]]

new_arr = rot_90(arr)
print(new_arr)
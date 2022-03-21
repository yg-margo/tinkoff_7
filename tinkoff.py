from itertools import permutations

n, k = map(int, input().split(" "))
st = input().split(" ")
gg = []
cnt = 0
arr = [''.join(x) for x in permutations(st, k)]
for i in range(0, len(arr)):
    ant = arr[i]
    gg.append(int(ant))
for i in range(0, len(ant)):
    z = gg[i] % 10
    gg[i] //= 10
    while gg[i] != 0:
        next_k = gg[i] % 10
        gg[i] //= 10
        if next_k < z:
            break
        else:
            cnt += 1
print(cnt)


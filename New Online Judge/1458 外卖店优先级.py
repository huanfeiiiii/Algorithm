# _*_ coding:utf-8 _*_

N, M, T = map(int, input().split())

arr = []
shops = [0] * N
for i in range(M):
    arr.append(list(map(int, input().split())))

d1 = {}
cache = []
for time, shop in arr:
    if time in d1:
        d1[time].append(shop)
    else:
        d1[time] = [shop]
d1 = sorted(d1.items(), key=lambda x: x[0])

for time, shop in d1:
    for j in range(len(shops)):
        if j + 1 in shop:
            shops[j] += 2 * shop.count(j+1)
        else:
            shops[j] = max(shops[j] - 1, 0)

    for i in range(len(shops)):
        if i not in cache and shops[i] > 5:
            cache.append(i)
            continue
        if i in cache and shops[i] <= 3:
            cache.remove(i)
            continue
    print(time, shop, shops, cache)

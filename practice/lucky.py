def isEqual(row):
    for i in 0, len(row)-2:
        for j in i+1, len(row)-1:
            # print("%d %d" % (i, j))
            if row[i] == row[j]:
                return True
    return False

# 总长度，位置
length, position = 4, 4

nums = input().split()

res = []
for num in nums:
    for i in range(1, 11):
        for j in range(1, 11):
            for k in range(1, 11):
                res.append([i, j, k, int(num)])

result = []
for i in range(len(res)):
    row = res[i]
    a1, a2, a3, a4 = row[0], row[1], row[2], row[3]
    if a1 == a2-1 and a2 == a3-1 and a3 == a4-1:
        continue
    if a1 == a2+1 and a2 == a3+1 and a3 == a4+1:
        continue
    if a1 > 5 and a2 > 5 and a3 > 5 and a4 > 5:
        continue
    if a1 < 6 and a2 < 6 and a3 < 6 and a4 < 6:
        continue

    if isEqual(row):
        continue

    result.append(row)


print("origin rows: %d, after filter: %d" % (len(res), len(result)))
print(result)

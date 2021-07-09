src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
ans = []
i = 0
for el in src:
    i += 1
    if src[i - 2] < src[i - 1]:
        ans.append(el)
print(ans)

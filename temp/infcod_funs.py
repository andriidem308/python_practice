from collections import Counter

s = "кодуваннякодудекодування"
cnt = Counter()
for c in s: cnt[c] += 1

print(len(s))
print(cnt)
import collections

S=input()
max=0
k=''
c=collections.Counter(S)
for i in c:
    if c[i]>max:
        max=c[i]
        k = i
print(max, ' ' ,k)
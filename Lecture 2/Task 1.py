n = list(map(int, input().split()))

a = [] * len(n)
for i in range(len(n)):
    if n[i] % 2 == 0:
        a.append(n[i])


b = [] * len(a)
for k in range(len(a)):
    if a[k] % 3 == 0:
        b.append(a[k])

print(b)

n = list(map(int, input().split())) #ввод массива через пробел, преобразование в int

a = [] * len(n) #массив четных чисел
for i in range(len(n)):
    if n[i] % 2 == 0: #проверка на четность
        a.append(n[i]) #добавление в массив a


b = [] * len(a) #массив четных чисел, делящихся на 3
for k in range(len(a)):
    if a[k] % 3 == 0: #проверка на делимость на 3
        b.append(a[k]) #добавление в массив b

print(b)

n = list(map(int, input().split())) #ввод массива через пробел, преобразование в int

a = [] #массив итоговых чисел
for i in range(len(n)):
    if n[i] % 2 == 0: #проверка на четность
        if n[i] % 3 == 0:
            a.append(n[i]) #добавление в массив a

for i in range(len(a)):
    print(a[i], end=' ')

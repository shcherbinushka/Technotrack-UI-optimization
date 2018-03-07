n = 0
def bubble_sort_rise(array):
    N = len(array)
    n = 0
    for bypass in range(1, N): ## bypass - номер прохода массива
        for k in range(0, N - bypass):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
                n += 1
    return array,n
        
def bubble_sort_set(array):
    N = len(array)
    n = 0
    for bypass in range(1, N): ## bypass - номер прохода массива
        for k in range(0, N - bypass):
            if array[k] < array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
                n += 1
    return array,n


print("Введите количество строк в двумерном массиве.")
lines = int(input())

A = []
for i in range(lines):
    A.append([0] * lines)

print("Введите элементы массива через пробел. Один массив - одна строка.")
for i in range(lines):
    A[i] = list(map(int, input().split()))

for i in range(len(A)):
    if i % 2 == 0:
        array = A[i]
        array,n1 = bubble_sort_rise(array)
        n += n1
        
    else:
        array = A[i]
        array,n2 = bubble_sort_set(array)
        n += n2
        
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()
    

print('Количество итераций =', n)

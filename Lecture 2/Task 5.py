n = 0
def bubble_sort(array):
    N = len(array)
    n = 0
    for bypass in range(1, N): ## bypass - номер прохода массива
        for k in range(0, N - bypass):
            if array[k] > array[k + 1]:
                array[k], array[k + 1] = array[k + 1], array[k]
                n += 1
    return array,n
        
print("Введите количество строк в двумерном массиве.") 
lines = int(input()) 
print("Введите количество элементов в строке") 
elements = int(input()) 

A = []


print("Введите элементы массива по одному в каждой строке.") 
print("Обратите внимание, что каждому массиву соответствует строго указанное количество элементов")
for i in range(lines): #ввод двумерного массива по одному элементу в строку
    A.append([]) 
    for j in range(elements): 
        el = int(input()) 
        A[i].append(el) 

for i in range(len(A)):
    if i % 2 == 0:
        array = A[i]
        array,n1 = bubble_sort(array)
        n += n1
        
    else:
        array = A[i]
        array,n2 = bubble_sort(array)
        array.reverse()
        n += n2
        
for i in range(len(A)):
    for j in range(len(A[i])):
        print(A[i][j], end=' ')
    print()
    

print('Количество итераций =', n)


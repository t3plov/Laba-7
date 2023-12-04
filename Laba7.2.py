import random

M = random.randint(1, 10) 
N = random.randint(1, 10) 
A = []
print('Кол-во строк:', M)
print('Кол-во столбцов:', N)
cell = []
a = 0
    
for i in range(M):
    for x in range(N):
        a = random.randint(-1000, 1000)
        cell.append(a)
    A = cell

B = [A[i:i + N] for i in range(0, len(A), N)]
print('Матрица до сортировки:')

for i in range(len(B)):
    print(B[i])
summ = []
for i in B:
    sum = 0
    for x in range(1, len(i), 2):
        if i[x] > 0:
            sum += i[x]
    summ.append(sum)
    
print()
print('Характеристики строк матрицы до сотрировки:')

for i in range(len(summ)):
    print(summ[i])

for i in range(len(summ) - 1):
    for x in range(i + 1, len(summ)):
        if summ[i] < summ[x]:
            B[i], B[x] = B[x], B[i]
            summ[i], summ[x] = summ[x], summ[i]
print()
print('Матрица после сортировки:')
for i in range(len(B)):
    print(B[i])
print()
print('Характеристики строк матрицы после сортировки:')
for x in range(len(summ)):
    print(summ[x])



            
            
    
        
    

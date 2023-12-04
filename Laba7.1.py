import random

try:
    M = random.randint(1, 10) 
    N = random.randint(1, 10) 
    A = []
    print('Кол-во строк', M)
    print('Кол-во столбцов', N)
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

    print('Матрица после сортировки:')
    
    for i in range(len(B)):
        if i % 2 != 0:
            print(B[i][::-1])
        else:
            print(B[i])
            
except ValueError:
    print('Ошибка')

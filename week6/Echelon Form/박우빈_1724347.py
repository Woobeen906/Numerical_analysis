from numpy import array, zeros, ones
import numpy as np

file = open("elementary_data.txt", "r")
matrix = []
for i in file.readlines():
    temp = list(map(int, i.split(" ")))
    matrix.append(temp)

n=len(matrix)
max=0
for i in range(n):  #배열의 크기가 3x3보다 큰지 파악
    m=len(matrix[i])
    if max<m:
        max=m

if max<=3: #배열의 크기가 3x3이면 작동
    all_temp = list(range(3))
    check = 0
    pivot = []
    for i in range(0, 3):
        for j in all_temp:
            if (matrix[j][i] != 0):
                pivot.append(matrix[j])
                all_temp.remove(j)
            else:
                check = 1

    if check == 0:
        max = -1
        pivot = matrix
        for i in range(3):
            if (max < pivot[i][0]):
                max = pivot[i][0]
                max_index = i

    pivot = (pivot) * ones((3, 3))

    for i in range(3):
        for j in range(i + 1, 3):
            if (pivot[i][i] != 0):
                mulvalue = pivot[j][i] / pivot[i][i]
                cal = pivot[i] * mulvalue
                pivot[j] = pivot[j] - cal
    print(pivot)

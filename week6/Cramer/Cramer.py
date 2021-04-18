from numpy.linalg import det
import copy

file_a = open("a_test_data.txt", "r")
a = []
for i in file_a.readlines():
    temp_a = list(map(int, i.split(" ")))
    a.append(temp_a)

file_b = open("b_test_data.txt", "r")
b = []
for i in file_b.readlines():
    temp_b = list(map(int, i.split(" ")))
    b.append(temp_b)

n = len(a)
a1 = copy.deepcopy(a)
a2 = copy.deepcopy(a)
a3 = copy.deepcopy(a)

for i in range(n):
    a1[i][0] = b[0][i]
    a2[i][1] = b[0][i]
    if n == 3:
        a3[i][2] = b[0][i]

detA = det(a)
detA1 = det(a1)
detA2 = det(a2)
if n == 3:
    detA3 = det(a3)
    x3 = detA3 / detA

print('|A| = ', detA, '|A1| = ', detA1, '|A2| = ', detA2)
if n == 3:
    print('|A3| = ', detA3)

x1 = detA1 / detA
x2 = detA2 / detA

print('x1 = ', x1, 'x2 = ', x2, 'x3 = ', x3)

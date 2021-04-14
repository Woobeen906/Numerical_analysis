from numpy import array, zeros, sign
import matplotlib.pyplot as plt


def f(x):
    return x ** 5 - 1


a = -2.0
b = 3.0
n = 14
y = zeros(n)
x = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
arr = zeros(n)

for i in range(n):
    y[i] = (a + b) / 2.0
    if sign(f(y[i])) == sign(f(a)):
        a = y[i]
    else:
        b = y[i]

for i in range(1, n):
    arr[i] = abs((((y[i] - y[i - 1]) / y[i])))
# printing output
print("%5s %8s %8s" % ('k', 'x', 'ε(%)'))
for k in range(n):
    print("%4d %9.4f %8.4f" % (k + 1, y[k], arr[k] * 100))

plt.plot(x, y, 'ko-')
plt.plot(x, arr, 'g--')
plt.xlabel('Iterations')
plt.ylabel('x')
plt.show()
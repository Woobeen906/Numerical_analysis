from numpy import array, linspace, zeros, sign, cos
import matplotlib.pyplot as plt


def f(x):
    return -x ** 2 + 6.0 * x - 5.0


a = -2.0
b = 3.0
n = 15
c = zeros(n)
x = array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])
error = zeros(n)

for i in range(n):
    c[i] = (a + b) / 2.0
    if sign(f(c[i])) == sign(f(a)):
        a = c[i]
    else:
        b = c[i]

for i in range(1, n):
    error[i] = abs((((c[i] - c[i - 1]) / c[i])))
# printing output
print("%5s %8s %8s" % ('k', 'c', 'ε(%)'))
for k in range(n):
    print("%5d %9.4f %8.4f" % (k + 1, c[k], error[k] * 100))

plt.plot(x, c, 'y--', label='c')
plt.plot(x, error, 'bo-', label='ε')
plt.legend()
plt.xlabel('Iterations')
plt.show()

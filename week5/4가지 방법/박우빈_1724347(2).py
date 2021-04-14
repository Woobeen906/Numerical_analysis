from numpy import zeros, array, cos, sin
import matplotlib.pyplot as plt


def f(x):
    return x ** 5 - 1


def df(x):
    return 5 * x ** 4


n = 15;
x0 = 3.0
x = zeros(n)
x[0] = x0
itl = range(1, 16)
it = array(itl)
arr = zeros(n)

for k in range(n - 1):
    x[k + 1] = x[k] - f(x[k]) / df(x[k])

for i in range(1, n):
    arr[i] = abs((((x[i] - x[i - 1]) / x[i])))
# printing output
print("%5s %8s %8s" % ('k', 'x', 'ε(%)'))
for k in range(n):
    print("%4d %9.4f %9.4f" % (k + 1, x[k], arr[k] * 100))

plt.plot(it, x, 'go')
plt.plot(it, arr, 'ro')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.show()
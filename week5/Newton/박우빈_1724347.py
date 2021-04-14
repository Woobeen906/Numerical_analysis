from numpy import zeros, array, cos, sin
import matplotlib.pyplot as plt


def f(x):
    return 3 * x - cos(x) - 1


def df(x):
    return 3 + sin(x)


n = 9;
x0 = 0.0
x = zeros(n)
x[0] = x0
itl = range(0, 9)
it = array(itl)
dftval = zeros(n)

for k in range(n - 1):
    x[k + 1] = x[k] - f(x[k]) / df(x[k])

for i in range(1, n):
    dftval[i] = abs((((x[i] - x[i - 1]) / x[i])))
# printing output
print("%5s %8s %8s" % ('k', 'x', 'ε(%)'))
for k in range(n):
    print("%4d %9.4f %9.4f" % (k + 1, x[k], dftval[k] * 100))

plt.plot(it, x, 'bo-')
plt.plot(it, dftval, 'yo-')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.show()
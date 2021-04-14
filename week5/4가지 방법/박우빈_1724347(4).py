from numpy import zeros, array, cos
import matplotlib.pyplot as plt


def f(x):
    return x ** 5 - 1


n = 10;
x = zeros(n)
x0 = 3.0
x1 = 6.0;
itl = range(1, 11)
it = array(itl)
arr = zeros(n)
arr[0] = 0

for k in range(n):
    x2 = x1 - f(x1) * ((x1 - x0) / (f(x1) - f(x0)))
    x0 = x1
    x1 = x2
    x[k] = x2

for i in range(1, n):
    arr[i] = abs((((x[i] - x[i - 1]) / x[i])))
# printing output
print("%5s %8s %8s" % ('k', 'x', 'ε(%)'))
for k in range(n):
    print("%4d %9.4f %9.4f" % (k + 1, x[k], arr[k] * 100))

plt.plot(it, x, 'go-')
plt.plot(it, arr, 'ko-')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.show()
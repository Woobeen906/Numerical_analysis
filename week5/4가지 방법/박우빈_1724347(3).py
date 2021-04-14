from numpy import array, zeros
import matplotlib.pyplot as plt


def g(x):
    return 1 / x ** 4


x0 = 1
n = 5
x = zeros(n)
x[0] = x0
itl = range(1, 6)
it = array(itl)
arr = zeros(n)

for i in range(n - 1):
    x[i + 1] = g(x[i])

for i in range(1, n):
    arr[i] = abs((((x[i] - x[i - 1]) / x[i])))
# printing output
print("%5s %8s %8s" % ('k', 'x', 'ε(%)'))
for k in range(n):
    print("%4d %9.4f %8.4f" % (k + 1, x[k], arr[k] * 100))

plt.plot(it, x, 'g')
plt.plot(it, arr, 'b')
plt.xlabel('Iteration')
plt.ylabel('x')
plt.show()
from numpy import array, zeros, cos
import matplotlib.pyplot as plt

def g(x):
    return (cos(x) + 1) / 3

x0 = 0.2
n = 10
x = zeros(n)
x[0] = x0
itl = range(1, 11)
it = array(itl)
error = zeros(n)

for i in range(n - 1):
    x[i + 1] = g(x[i])

for i in range(1, n):
    error[i] = abs((((x[i] - x[i - 1]) / x[i])))
# printing output
print("%5s %8s %8s" % ('k', 'x', 'ε(%)'))
for k in range(n):
    print("%4d %9.4f %8.4f" % (k + 1, x[k], error[k] * 100))

plt.plot(it, x, 'y')
plt.plot(it, error, 'b')
plt.xlabel('Iteration')
plt.show()
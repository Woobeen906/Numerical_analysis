from numpy import zeros
import matplotlib.pyplot as plt

n = 10;
x1 = zeros(n)
x2 = zeros(n)
x3 = zeros(n)

relative1 = zeros(n)
relative2 = zeros(n)
relative3 = zeros(n)
it = range(n)

print('%7s %9s %9s %9s %9s %9s %9s' % ('k','x1','x2','x3','re1','re2','re3'))
print('%7s %9.5f %9.5f %9.5f %9.5f %9.5f %9.5f' % (0, x1[0], x2[0], x3[0], relative1[0], relative2[0], relative3[0]))

for k in range(n-1):
    x1[k + 1] = (-1.0 + 2.0 * x2[k] - 3.0 * x3[k]) / 5.0
    x2[k + 1] = (2.0 + 3.0 * x1[k] - x3[k]) / 9.0
    x3[k + 1] = (-3.0 + 2.0 * x1[k] - x2[k]) / 7.0

    relative1[k + 1] = abs(((x1[k + 1] - x1[k]) / x1[k + 1]))
    relative2[k + 1] = abs(((x2[k + 1] - x2[k]) / x2[k + 1]))
    relative3[k + 1] = abs(((x3[k + 1] - x3[k]) / x3[k + 1]))
    print('%7s %9.4f %9.4f %9.4f %9.4f %9.4f %9.4f' % (k + 1, x1[k + 1], x2[k + 1], x3[k + 1], relative1[k + 1], relative2[k + 1], relative2[k + 1]))

plt.plot(it, x1, 'b-', label ='x1j')
plt.plot(it, x2, 'g--', label ='x2j')
plt.plot(it, x3, 'ko-', label ='x3j')
plt.plot(it, relative1, 'k', label ='relative1')
plt.plot(it, relative2, 'y', label ='relative2')
plt.plot(it, relative3, 'r', label ='relative3')
plt.legend()
plt.xlabel('iteration')
plt.ylabel('Approxiimate Solutions')
plt.show()
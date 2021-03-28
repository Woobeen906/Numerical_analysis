from numpy import linspace
import matplotlib.pyplot as plt

def f(x):
    return -x**2+6.0*x-5.0

x=linspace(0,7)

plt.plot(x,f(x),'d')
plt.plot(0,0,'b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('-x**2+6*x-5')
plt.show()



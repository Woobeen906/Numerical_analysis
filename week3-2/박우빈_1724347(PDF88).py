from numpy import linspace,cos
import matplotlib.pyplot as plt

def f(x):
    return 3*x-cos(x)-1

x=linspace(-1,5)

plt.plot(x,f(x),'d')
plt.plot(0,0,'b')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('3*x-cos(x)-1')
plt.show()



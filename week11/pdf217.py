from numpy import mean , median, var,std,array
import matplotlib.pyplot as plt
t=array([1,2,3,4,5,6,7])
x= array([20,23,25,22,21,19,18])

mu=mean(x) #평균
med=median(x) #중앙값
vari=var(x) # 분산
stdd=std(x) # 표준편차

print('평균 = %6.2f' %mu)
print('중앙값 = %6.2f' % med)
print('분산 = %6.2f' %vari)
print('표준편차 = %6.2f' %stdd)

plt.plot(t,x,'ko-')
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.show()
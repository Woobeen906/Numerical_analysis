from numpy import *

Arr1=array([arange(1,2),arange(3,4),arange(5,6)])
Arr2=array([[2,3,5],[1,7,8],[-1,-2,-3]])

issame=(Arr1 is Arr2)
print(issame)
#같은지

add=Arr1 + Arr2
print(add)
#덧셈

mul=Arr1 * Arr2
print(mul)
#곱셈

sub=Arr1-Arr2
print(sub)
#뺼셈

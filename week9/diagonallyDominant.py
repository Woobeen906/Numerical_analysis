from numpy import array

Arr1=array([[5,-2,3],[-3,9,1],[-2,1,7]])
Arr2=array([[5,-2,3],[-2,1,7],[-3,9,1]])

def diagonallyDominant(x):
    k=0
    index=0
    temp=0
    for i in x:
        temp=0
        for j in i:
            if (j != i[index]):
                temp += abs(j)

        if(abs(i[index])>=temp):
            k+=1
        index+=1

    if(k>=3):
        return True
    else:
        return False


print(diagonallyDominant(Arr1))
print(diagonallyDominant(Arr2))
import txt as txt
from numpy import array, zeros, ones, floor
import numpy as np
from tkinter import filedialog
from tkinter import *
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)
# 버전차이로 파일 리더시 필요
root = Tk()

root.title('Gauss')
root.geometry("500x500")
root.resizable(True, True)


matrix = []


lbl = Label(root, text="파일 경로")
lbl.pack()

txt = Label(root, text=" ",width=70,heigh=1,fg="green",relief="solid")
txt.pack()


def Save():
	root.dirName=filedialog.askopenfilename()
	print (root.dirName)
	txt.configure(text="입력 파일 경로: " + root.dirName)

btn=Button(root,width=10,text="파일 선택",command=Save)
btn.pack()

def Gauss():
    with open(root.dirName, 'r') as f:
        for row in f.read().strip().split("\n")[0:]:
            matrix.append(row.split(" "))
    a = len(matrix)
    b = len(matrix[0])
    pivot = [[0] * b for _ in range(a)]
    check = 0
    for i in range(a):
        for j in range(b):
            pivot[i][j] = int(matrix[i][j])
    temp = []
    for i in range(a):
        check = i
        if (pivot[i][check] == 0):
            for k in range(i + 1, a):
                if (pivot[k][check] != 0):
                    temp.append(pivot[k])
                    pivot[k] = pivot[i]
                    pivot[i] = temp[0]
                    temp.clear()
                    break

        for j in range(i + 1, a):
            if (pivot[i][check] == 0):
                continue
            else:
                t = pivot[j][check] / pivot[i][check]
            for r in range(b):
                pivot[j][r] -= t * pivot[i][r]

        check += 1



    x = [[1] * 1 for _ in range(a)]
    for i in range(a):
        x[i] = float(1)

    for i in reversed(range(a)):
        t = float(pivot[i][-1])
        temp2 = 1
        for j in range(b - 1):
            if (i == j):
                temp2 = pivot[i][j]
            else:
                t -= x[j] * pivot[i][j]
        x[i] = t / temp2

    label=Label(root,text="가우스 소거법 처리된 행렬")
    label.pack()
    for i in range(a):
        for j in range(b):
            pivot[i][j]=round(pivot[i][j],2)

    result=[]
    for i in range(a):
        result.append(pivot[i])

    result.append(x)

    print(result)
    np.savetxt('gauss_output.txt', result, fmt='%s')
    for i in range(a):
        label=Label(root,width=50,text=pivot[i])
        label.pack()

    for i in range(a):
        x[i]=round(x[i],4)

    for i in range(a):
        print(pivot[i])

    print("x=", x)
    xRes=Label(root,text="구하는 해")
    xRes.pack()
    for i in range(a):
         xLabel=Label(root,text=x[i])
         xLabel.pack()

btn2=Button(root,width=10,text="실행",command=Gauss)
btn2.pack()

result=Label(root,text="결과창")
result.pack()


root.mainloop()


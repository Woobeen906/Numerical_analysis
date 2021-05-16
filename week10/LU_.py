import numpy as np
from tkinter import filedialog
from tkinter import *
import txt as txt
import warnings
warnings.filterwarnings("ignore", category=np.VisibleDeprecationWarning)


root = Tk()

root.title('LU분해')
root.geometry("500x600")
root.resizable(True, True)


#matrix = np.loadtxt('LU_Input.txt')
matrix=[]

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

def LU():
    with open(root.dirName, 'r') as f:
        for row in f.read().strip().split("\n")[0:]:
            matrix.append(row.split(" "))
    a = len(matrix)
    b = len(matrix[0])

    U = [[0] * a for _ in range(a)]
    L = [[0] * a for _ in range(a)]
    Y = [[0] * 1 for _ in range(a)]

    for i in range(a):
        Y[i] = float(matrix[i][-1])

    LT = np.eye(a)

    for i in range(a):
        for j in range(a):
            L[i][j] = float(LT[i][j])

    C = [[0] * 1 for _ in range(a)]

    for i in range(a):
        C[i] = float(matrix[i][-1])

    for i in range(a):
        for j in range(a):
            U[i][j] = int(matrix[i][j])
    temp = []

    check = False
    for i in range(a - 1):
        if (U[i][i] == 0):
            for k in range(i + 1, a):
                if (U[k][i] != 0):
                    temp.append(U[k])
                    U[k] = U[i]
                    U[i] = temp[0]
                    temp.clear()
                    break

        for j in range(i + 1, a):
            if (U[i][i] == 0):
                if (i < a - 1):
                    check = True
                continue
            t = U[j][i] / U[i][i]
            for k in range(a):
                if (U[i][k] == 0):
                    U[j][k] -= t * U[i][k]
                    continue
                L[j][k] += U[j][k] / U[i][k] * L[i][k]
                U[j][k] -= t * U[i][k]

    print("L=", L)
    print("U=", U)
    result = []
    result.append("L")
    Llabel=Label(root,text="분해된 L")
    Llabel.pack()
    for i in range(a):
        Lresult=Label(root,text=L[i])
        Lresult.pack()
        result.append(L[i])

    result.append("\n")
    result.append("U")
    Ulabel=Label(root,text="분해된 U")
    Ulabel.pack()
    for i in range(a):
        Uresult = Label(root, text=U[i])
        Uresult.pack()
        result.append(U[i])

    # L
    Ly = [[1] * 1 for _ in range(a)]

    for i in range(a):
        Ly[i] = float(1)
    for i in range(a):
        t = float(Y[i])
        temp = 1
        for j in range(a):
            if (i == j):
                temp = L[i][j]
            else:
                t -= L[i][j] * Y[j]
        Y[i] = t / temp
    print('Y의 해는',Y)

    Ux = [[1] * 1 for _ in range(a)]
    X = [[1] * 1 for _ in range(a)]


    Ylabel=Label(root,text='Y')
    Ylabel.pack()
    for i in range(a):
        Yresult=Label(root,text=Y[i])
        Yresult.pack()
        X[i] = Y[i]

    for i in reversed(range(a)):
        t = float(X[i])
        temp2 = 1
        for j in range(a):
            if (i == j):
                temp2 = U[i][j]
            else:
                t -= X[j] * U[i][j]
        X[i] = t / temp2

    print('X의 해는 ',X)
    Xlabel = Label(root, text='X')
    Xlabel.pack()
    for i in range(a):
        Xresult = Label(root, text=X[i])
        Xresult.pack()

    result.append("\n")
    result.append("Y")
    for i in range(a):
        result.append(Y[i])

    result.append("\n")
    result.append("X")
    for i in range(a):
        result.append(X[i])
    np.savetxt('LU_Out.txt', result, fmt='%s')

btn2=Button(root,width=10,text="실행",command=LU)
btn2.pack()

root.mainloop()
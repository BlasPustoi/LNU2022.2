import numpy as np
import time
#A=[[1,2,3,4,5,6,7,8,9,10],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1]]
#B=[[1,2,3,4,5,6,7,8,9,10],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1],[5,6,7,8,9,7,8,5,4,1]]
A=np.random.random((200,200))
B=np.random.random((200,200))
s=(len(B),len(A[0]))
C=np.zeros(s)
def mult(A,B,C):
    if(len(A[0])!=len(B)):
        return 0
    for i in range(len(B)):
        for j in range(len(A[0])):
            for k in range(len(A[0])):
                C[i][j]=C[i][j]+A[i][k]*B[k][i]
    return C
start=time.time()
mult(A,B,C)
end=time.time()
print(end-start)
start=time.time()
np.dot(A,B)
end=time.time()
print(end-start)
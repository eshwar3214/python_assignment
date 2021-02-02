# name   : sai eshwar reddy kottapally
# rollno : 100519733022
# program to calculate the product of two n*n matrices

import numpy as np 

n=eval(input("enter the order of the square matrices:"))

a=np.array([0 for i in range(n)]for j in range(n))
b=np.array([0 for i in range(n)]for j in range(n))
 
for i in range(n):
    for j in range(n):
        a[i][j]=eval(input("a["+str(i)+"]["+str(j)+"]"))

print(a)
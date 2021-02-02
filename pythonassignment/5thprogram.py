# name   : sai eshwar reddy kottapally
# rollno : 100519733022
# program to find the roots of a quadratic equation

from math import *

#eqn is of the form ax2+bx+c=0
a=eval(input("enter the co-efficent of x2:"))
b=eval(input("enter the co-efficent of x:"))
c=eval(input("enter the constant:"))

print("roots of the given equation are",((-b+sqrt((b**2)-(4*a*c)))/(2*a)),((-b-sqrt((b**2)-(4*a*c)))/(2*a)))
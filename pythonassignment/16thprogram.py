# name    : sai eshwar reddy kottapally
# rollno  : 100519733022
# program to reverse a list without reverse function

L1=[]
n=eval(input("enter the size of the list:"))

for i in range(n):
    L1.append(eval(input("enter the values:")))

print("reversed elements of the list")
for i in range(n):
    print("",L1[n-1-i],end="")


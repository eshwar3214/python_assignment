# name:sai eshwar reddy kottapally
# roll no:100519733022
# program to print numbers greater than a number in a list

a=[]
size=eval(input("enter size of the list:"))
n=eval(input("enter a number:"))


for i in range(size):
    a.append(eval(input("a["+str(i)+"]")))

def greater_than_n(list,number):
    print("elements of the list greater than",n,"are")
    for i in range(size):
        if a[i]>n:
            print(a[i])

greater_than_n(a,n)
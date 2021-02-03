# name   : sai eshwar reddy kottapally
# rollno : 100519733022
# program to print all unique elements of a list

list=[]

n=eval(input("enter the size of the list:"))

for i in range(n):
    list.append(eval(input("enter the elements:")))

print("unique elements of the list are:")

for i in range(n):
    count=list.count(list[i])
    if(count==1):
        print(list[i])
        

        
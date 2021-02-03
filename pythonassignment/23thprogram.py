# name    : sai eshwar reddy kottapally
# rollno  : 100519733022
# program to print duplicates of a list

list=[]

n=eval(input("enter the size of the list:"))

for i in range(n):
    list.append(eval(input("enter the elements:")))

dupitems=[]
uniqitems={}
for x in list:
    if x not in uniqitems:
        uniqitems[x]=1
    else:
        if uniqitems[x]==1:
            dupitems.append(x)
        uniqitems[x]+=1

print(dupitems)   


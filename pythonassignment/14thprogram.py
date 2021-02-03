# name    : sai eshwar reddy kottapally
# rollno  : 100519733022
# program with a function that takes two lists and outputs pairwise sum of the lists

list1=[1,2,3,4,5]
list2=[6,7,8,9,10]


def addlists(a,b):
    c=[]
    for i in range(len(a)):
         c.append(a[i]+b[i])
    return c

print(addlists(list1,list2))


# name    : sai eshwar reddy kottapally
# rollno  : 100519733022
# program to find the second smallest number of a list

list=[5,4,5,6,7,8,9,10,44,3]

def secondsmallest(a):
    a.sort()
    print(a[a.index(min(a))+1])

secondsmallest(list)

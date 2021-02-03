# name    : sai eshwar reddy kottapally
# rollno  : 100519733022
# program to find the second largest number of a list

list=[2,2,4,5,6,7,8,9,22,19]

def secondsmallest(a):
    a.sort()
    print(a[a.index(max(a))-1])

secondsmallest(list)

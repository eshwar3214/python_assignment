# name   : sai eshwar reddy kottapally
# rollno : 100519733022
# program to find how many elements are divisible by 2,3,4,5,6,7 in between 1 and 1000


def no_of_elements_divisible(n):
    count=0
    for i in range(1000):
        if i%n==0:
            count=count+1
    return count

for i in range(2,8):
    print("no_of_elements_divisible by "+str(i)+"are",no_of_elements_divisible(i))


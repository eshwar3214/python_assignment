# name   : sai eshwar reddy kottapally
# rollno : 100519733022
# program to find mean median mode of a list


import statistics

list=[]
n=eval(input("enter the size of the list:"))


for i in range(n):
    list.append(eval(input("enter the elements:")))

print(list)

print("mean of the list:",statistics.mean(list))
print("median of the data:",statistics.median(list))
print("mode of the data:",statistics.mode(list))

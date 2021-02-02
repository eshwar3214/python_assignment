n=eval(input("enter the set size:"))
a=[]
for i in range(n):
    a.append(eval(input("enter values a["+str(i)+"]:")))

a.sort()
print("largest number in the list is",a[-1])
print("second largest number in the list is",a[-2])

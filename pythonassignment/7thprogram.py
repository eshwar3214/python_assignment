# name:sai eshwar reddy kottapally
# roll no:100519733022
# program to use recursive and non recursive functions to find gcd

# program to find gcd of two numbers non recursively
def gcd(a,b):
       if a==b:
              gcd=a
              mul=gcd
       if a<b:
              for i in range (1,a+1):
                    if a%i==0 and b%i==0:
                        mul=i
       if b<a:
            for i in range (1,b+1):
                    if a%i==0 and b%i==0:
                        mul=i
       print('Greatest common factor of',a,'and',b,'is',mul)
a=eval(input('enter a : '))
b=eval(input('enter b : '))
gcd(a,b)

#Output:
#enter a : 6
#enter b : 36
#Greatest common factor of 6 and 36 is 6


#7.Program to find GCD of two integers recursively
def gcdr(a,b):
    if a<b:
        a,b=b,a
    if b!=0:
          return gcdr(b,a%b)
    else:
              return a
a=eval(input('enter a : '))
b=eval(input('enter b : '))
print('The gcd of ',a,' and ',b,' is ',gcdr(a,b))

'''0utput:
enter a : 20
enter b : 4
The gcd of  20  and  4  is  4'''

# non Recursive function to print factorial of a positive number
def fact(n):
       mul=1
       for i in range (1,n+1):
              mul=mul*i
              i+=1
       return mul
n=eval(input('enter a positive integer : '))
print('Factorial of ',n,' is ',fact(n))

'''Output:
enter a positive integer : 5
Factorial of  5  is  120'''

#Recursive function to print factorial of a positive number
def fact(n):
       if n==0:
              return 1
       else:
              return n*fact(n-1)
n=eval(input('Enter a positive integer : '))
print('Factorial of ',n,' is ',fact(n))

'''Output:
Enter a positive integer : 6
Factorial of  6  is  720'''

#fibbonaci series without recursion
# Enter number of terms needed                   #0,1,1,2,3,5....
a=int(input("Enter no of terms :"))
f=0                                         #first element of series
s=1                                         #second element of series
if a<=0:
    print("The requested series is",f)
else:
    print(f,s,end=" ")
    for x in range(2,a):
        next=f+s                           
        print(next,end=" ")
        f=s
        s=next

print("\n")
	   
#fibonacci series usig recursion
def fib(n):
       if n==1:
              return 1
       if n==0:
              return 0
       else:
              return fib(n-2)+fib(n-1)
n=eval(input('Enter a positive integer : '))
print('Fibonacci series is : ')
for i in range (0,n):
       print(fib(i))


#  non-recursive program to convert decimal number to binary 
n=int(input("Enter a number: "))
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()
print("Binary Equivalent is: ")
for i in a:
    print(i,end='')

# recursive program to convert decimal number to binary
def convertToBinary(x):
    if x> 1:
        convertToBinary(x//2)
    print(x%2,end = '')

# decimal number

x=eval(input("\nenter a number:"))
print("binary equivalent is:")
convertToBinary(x)
print()
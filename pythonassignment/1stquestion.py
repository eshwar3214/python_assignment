# name:sai eshwar reddy kottapally
# roll no:100519733022
# program to print sum of prime numbers under 100

sum=0
for i in range(2,100):
    isprime=1
    for j in range(2,i):
        if(i%j==0):
            isprime=0
            break
    if(isprime==1):
        sum=sum+i
        
print("sum of prime numbers under 100:",sum)

    

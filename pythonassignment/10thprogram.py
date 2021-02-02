# name   : sai eshwar reddy kottapally
# rollno : 100519733022
# program to count no of vowels and consonants in a given string


import string

k=input("enter a string:")
k=k.lower()
vowels=['a','e','i','o','u']
consonants=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']


def no_of_vowels(str):
    cvow=0
    for i in range(len(k)):
        if k[i] in vowels:
            cvow=cvow+1
    return cvow
    

def no_of_consonants(str):
    ccons=0
    for i in range(len(k)):
        if k[i] in consonants:
            ccons=ccons+1
    return ccons
        
print("no of vowels:",no_of_vowels(k))
print("no of consonants:",no_of_consonants(k))


    

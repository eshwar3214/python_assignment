# name   : sai eshwar reddy kottapally
# rollno : 100519733022
# program to find whether a string is palindrome or not

import string

s=input("enter a string:")

ispalindrome=1

for i in range(len(s)):
    if s[i]!=s[len(s)-1-i]:
        ispalindrome=0

if ispalindrome==1:
    print("given string is a palindrome")
else :
    print("entered string is not a palindrome")
        

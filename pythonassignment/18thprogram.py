#name : sai eshwar reddy kottapally
#rollno: 100519733022
#program to write content in a file  and display it with a line number following colon



file1 = open('myfile.txt', 'w') 
Lst = ["This is myfile.txt file \n", "This is created to illustrate writing of files in python \n", "Let's see if it is done properly! \n"] 
file1.writelines(Lst) 
file1.close() 
  
# Checking if the data is written or not! 
file1 = open('myfile.txt', 'r')
print(file1.read()) 
file1.close()
#to print line with linenumber followed by colon!
file1 = open('myfile.txt', 'r')
line=file1.readline()
linenumber=1
while line!="":
    print( str(linenumber) + ":",line.rstrip("\n"))
    line=file1.readline()
    linenumber=linenumber+1


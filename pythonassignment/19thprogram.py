# name: sai eshwar reddy kottapally
# rollno: 100519733022
# Program to analyse the two text files using set operations

file1=set(open('myfile.txt'))
file2=set(open('file2.txt'))
print("Union:",file1.union(file2))
print("Intersection:",file1.intersection(file2))
print("Difference:",file1.difference(file2))


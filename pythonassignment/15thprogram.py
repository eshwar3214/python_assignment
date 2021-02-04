# name  : sai eshwar reddy kottapally
# rollno: 100519733022
# program to print all unique words in a text file



text_file = open('data.txt', 'r')
text = text_file.read()

# data.txt=Apple is a very big company. An apple a day keeps doctor away. A big fat cat came across the road beside doctor's office.
# The doctor owns apple device.

#cleaning
text = text.lower()
words = text.split()
words = [word.strip('.,!;()[]') for word in words]
words = [word.replace("'s", '') for word in words]

#finding unique
unique = []
for word in words:
    if word not in unique:
        unique.append(word)

#sort
unique.sort()

#print
print(unique)

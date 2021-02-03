# name   : sai eshwar reddy kottapally
# rollno : 100519733022
# program to print no of occurances in the given string

s=input("enter a string:")

def count_char(text):
    for i in range(len(text)):
        if len(text) == 0:
            break
        ch = text[0]
        if ch == ' ' or ch == '\t':
            continue
        print(ch + " - ", text.count(ch))
        text = text.replace(ch, '').strip()

count_char(s)

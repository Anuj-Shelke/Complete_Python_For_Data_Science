#Write a program to give Different inputs to same key and see what happens
d ={}
name = input("Enter Your name")
lang = input("Enter Your Language")
d.update({name:lang})
name = input("Enter Your name")
lang = input("Enter Your Language")
d.update({name:lang})
print(d)



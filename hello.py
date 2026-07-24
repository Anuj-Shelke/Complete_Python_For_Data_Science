#Program to find Greatest of four numbers Entered by the user ;
a = int(input('Enter number : ' ))
b = int(input('Enter number 2 : '))
c = int(input('Enter number 3 : '))
d = int(input("Enter number 4 : "))
if(a>b and a>c and a>d):
    print("A is greatest among the four")
elif(b>c and b>d):
    print("B is greatest among the four ")
elif(c>d):
    print("C is greatest among the four")
else:
    print("D is greatest")



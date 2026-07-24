#Program to find greatest of three numbers using function  ;
def greatest_of_three_numbers(a,b,c):
    if(a>b and a >c):
        print("A is the greatest number ")
    elif(b>c):
        print("B is the greatest number")
    else:
        print("C is the greatest number ")

a = int(input("Enter number 1"))
b = int(input("Enter number 2"))
c = int(input("Enter number 3"))
greatest_of_three_numbers(a,b,c)





    



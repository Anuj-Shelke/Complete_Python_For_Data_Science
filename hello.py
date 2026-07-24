#Program to check if student is pass or fail ;
maths = int(input("Enter marks of Maths"))
chem = int(input("Enter marks of Chem"))
phy = int(input("Enter marks of Physics "))

if(chem >= 33 and phy >= 33 and maths >= 33):
    if((maths+chem+phy/3)>=40):
        print("You are pass ")
else:
    print("Sorry try again next time")

#OOPs in Python 
class programmer:
    def __init__(self,n):
        self.n = n 

    def square(self):
        print("The square of the number is :",self.n*self.n)
    def cube(self):
        print("The cube of the number is :",self.n*self.n*self.n)
    def square_root(self):
        print("The square root of num is :",self.n**0.5)
    
    
print("Enter number to get all the parameters of :")
n= int(input("Enter the number "))
num = programmer(n)
num.square()
num.cube()
num.square_root()










    



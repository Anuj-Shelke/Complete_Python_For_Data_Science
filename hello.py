#Program to print sum of first n natural numbers Using recursive function  ;
def sum(n):
   if(n==1):
      return 1
   return sum(n-1)+n
n = int(input("Enter your number"))
print("sum of first n natural numbers is ",sum(n))
      




    



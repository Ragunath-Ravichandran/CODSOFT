
def add(x,y):
      print(x, "+", y, "=",x+y)
      
def sub(x,y):
       print(x, "-", y, "=",x-y)
def mul(x,y):
      print(x, "*", y, "=",x*y)
def div(x,y):
      print(x, "/", y, "=",x/y)


print("1.Addition")
print("2.Subraction")
print("3.Multiplication")
print("4.Division")


while True :
        c=int(input("enter the choice"))
        
        
        if (c<=0 or c>4):
          print("invalid enter correct choice")
          break
        else:
            a=float(input("enter the value"))
            b=float(input("enter the value"))
          
        
    
        if(c==1):
            add(a,b)
           
        elif(c==2):
           sub(a,b)
        elif(c==3):
          mul(a,b)
        elif(c==4):
          div(a,b)
        
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    
        
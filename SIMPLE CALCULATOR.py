
def add(x,y):
      print(x, "+", y, "=",x+y)
      
def sub(x,y):
       print(x, "-", y, "=",x-y)
def mul(x,y):
      print(x, "*", y, "=",x*y)
def div(x,y):
      print(x, "/", y, "=",x/y)


print("1.addition")
print("2.subraction")
print("3.multiplication")
print("4.division")


while True :
        c=int(input("enter the choice"))
        if (c<=0 or c>4):
          print("invalid enter correct choice")
        a=int(input("enter the value"))
        b=int(input("enter the value"))
    
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
    
        

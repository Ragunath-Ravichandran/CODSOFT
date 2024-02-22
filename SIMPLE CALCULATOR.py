def calculator():
    def add(x,y):
      print(x+y)
    def sub(x,y):
       print(x-y)
    def mul(x,y):
      print(x*y)
    def div(x,y):
      print(x/y)
    def pow(x,y):
      print(x**y)
    print("1.addition")
    print("2.addition")
    print("3.addition")
    print("4.addition")
    print("5.addition")
    
    c=int(input("enter the choise"))
    if (c<=0 or c>5):
      print("invalid enter correct choise")
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
    else:
      pow(a,b)
    print("operation calculated")
calculator()


       

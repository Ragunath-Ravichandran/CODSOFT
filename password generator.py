import random
def password_generator(len):
    password=""
    list=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9''a', 'b', 'c', 'd', 'e', 'f', 'g', 'h','i', 'j', 'k', 'm', 'n', 'o', 'p', 'q','r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H','I', 'J', 'K', 'M', 'N', 'O', 'P', 'Q','R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'z','@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>','*', '(', ')', '<']
    for i in range(0,len):
        password+=random.choice(list)
    print(password)
def pass_word():
    len=int(input("enter the leangth"))
    password_generator(len)
pass_word()
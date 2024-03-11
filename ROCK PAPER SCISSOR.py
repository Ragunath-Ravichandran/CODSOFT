import random

while True:
    print("1.rock")
    print("2.paper")
    print("3.scissor")
    user = int(input("Enter a choice"))
    if(user<=3):
       actions = [1,2,3]
       c=["rock","paper","scissor"]
       computer_action = random.choice(actions)
       print(user)
       print("computer_action=",c[computer_action-1])
       if user == computer_action:
        print("It's a tie!")
       elif user == 1:
        if computer_action == 3:
            print("You win!")
        else:
            print("You lose")
       elif user == 2:
        if computer_action ==1:
            print("You win!")
        else:
            print("You lose.")
       elif user == 3:
        if computer_action ==2:
            print("You win!")
        else:
            print("You lose.")
    else:
       print("invalid")
    play_again = int(input("Play again? (1.yes/2.no): "))
    if(play_again==1 or 2):
       if(play_again!=1):
        break
    else:
       print("enter the correct option")
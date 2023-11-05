import random

while True:
    choice = ["rock","paper","scissors"]

    computer = random.choice(choice)
    player = None

    print (computer)

    while player not in choice:
        player = input("rock paper or scissors? ").lower()
    
          

    if player == computer:
        print("computer: ",computer)
        print("player:",player)
        print("its a tie!")
    elif player == "rock":
        if computer == "scissors":
            print("computer: ",computer)
            print("player:",player)
            print("you win")
        if computer == "paper":
            print("computer: ",computer)
            print("player:",player)
            print("i win :)")
    elif player == "paper":
        if computer == "scissors":
            print("computer: ",computer)
            print("player:",player)
            print("i win")
        if computer == "rock":
            print("computer: ",computer)
            print("player:",player)
            print("you win")
    elif player == "scissors":
        if computer == "paper":
            print("computer: ",computer)
            print("player:",player)
            print("you win")
        if computer == "rock":
            print("computer: ",computer)
            print("player:",player)
            print("you win")

    play_again = input("play again? ")


    if play_again != "yes":
        break
 

import random
q = input("Press q to quit: ")
# Here I have given user an input to play as many times he want through a while loop
# to quit the user has to type Q
while q.lower() != "q":
    print("\t\t\tWelcome to Rock paper scizors\t")
    name = input("What is your name? ")
    # the variable stores a list of possible choices
    g = ["r", "p", "s"]
    # No. of rounds user wants to play
    rounds = int(input("How many rounds do you want? "))
    # Default values
    computer_win = 0
    player_win = 0
    draw = 0
    # Instructions
    print("\t\t*Instructions*")
    print("\n\t\tPress r for rock\n\t\tPress p for paper\n\t\tPress s for scissor")
    # In each outcome 1 round will be deducted and when it will reach 0 it will sgow results
    # I have increased the score of player if player wins,  also increased the score of computer if it wins and added no. of draws if it is a draw
    while rounds != 0:
        player_input = input("\n")
        # here I have used random to make the computer make a random choice among items in the list g
        if player_input.lower() == random.choice(g):
            print("Both showed the same!\nDraw")
            draw +=1
            rounds -=1
        elif player_input.lower() == "r" and random.choice(g) == "s":
            print(f"Computer showed scissor!\n--{name} throwed rock on the scissor!--")
            print(f"{name} won")
            rounds -=1
            player_win +=1
        elif player_input.lower() == "r" and random.choice(g) == "p":
            print(f"Computer showed paper!\n--Computer caught the rock!--")
            print("Computer won")
            rounds -=1
            computer_win +=1
        elif player_input.lower() == "p" and random.choice(g) == "r":
            print(f"Computer showed rock!\n--{name} caught the rock!--")
            print(f"{name} won")
            rounds -=1
            player_win +=1
        elif player_input.lower() == "p" and random.choice(g) == "s":
            print("Computer showed scissor!\n--Computer teared the paper!--")
            print("Computer won")
            rounds -=1
            computer_win +=1
        elif player_input.lower() == "s" and random.choice(g) == "r":
            print(f"Computer showed rock!\n--Computer throwed rock on the scissor!--")
            print("Computer won")
            rounds -=1
            computer_win +=1
        elif player_input.lower() == "s" and random.choice(g) == "p":
            print(f"Computer showed scissor!\n--{name} teared the paper!--")
            print(f"{name} won")
            rounds -=1
            player_win +=1
        else:
            print("It's a invalid input")
            
    # Scores -
    print("------------------------------------")
    print("Game Over!!")
    print(f"\n{name} scores: {player_win}\nComputer score: {computer_win}\nDraws: {draw}")
    
    # Displaying scores according to who wins
    
    if player_win > computer_win:
        print(f"{name} wins to computer by {player_win} to {computer_win}")
    elif player_win < computer_win:
        print(f"Computer wins to {name} by {computer_win} to {player_win} ")
    else:
        print("Its a draw")
    # asking user if he wants to play again or quit
    q = input('press q to quit: ')
    q = input("Press q to quit: ")

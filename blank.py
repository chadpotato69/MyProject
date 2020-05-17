import random
import time
minimum=1
maximum=10
generating_number=True
guessing_section=True


print("The Guessing Number Game")
print("Computer will generate a number and you have to guess it. \nThe range is 1 to 10")

response=input("Do you want to play? (Answer yes or no)")
while response not in ["yes","no"]: response=input("Invalid input. Answer with yes or no :")
if response== "yes":
    generating_number==True

elif response=="no":
    generating_number=False
    print("Bye-bye dear friend")

while generating_number:
    print("Game Starts")
    print("Generating a number.....")
    time.sleep(random.randint (1,5))#wait between 1 to 4 seconds randomly
    result=random.randint(minimum, maximum)
    print(result)
    generating_number=False
    player_guess =int(input("Do your best to guess."))

    while guessing_section:

        if player_guess>result:
            print("Your guess is too high.")
            player_guess =int(input("Try again"))
            continue
        elif player_guess<result:
            print("Your guess is too low.")
            player_guess =int(input("Try again"))
            continue
        elif player_guess==result:
            print("Congratulation! Your answer is correct")
        break
    play_again=input("Do you want to play again? (Yes or no)")
    if play_again=="yes":
        generating_number==True
        continue
    elif play_again=="no":
        generating_number=False
        print("Bye-bye. It is fun to play with you")

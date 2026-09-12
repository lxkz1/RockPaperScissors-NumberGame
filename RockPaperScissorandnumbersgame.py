import sys
import random
import art

def main():
    print(art.text2art("Welcome To Luca's Games"))
    print("Please insert 1 for Rock Paper Scissors and 2 for The Mythical Number Guessing Game")
    game_choice = get_game()
    if game_choice == "2":
        print(art.text2art("Excellent Choice!"))
        print("Here are the rules the game:")
        numbergame_instructions()
    elif game_choice == "1":
        print(art.text2art("Excellent Choice!"))
        print("Here are the rules for the game:")
        rockpaperscissors_instructions()
    else:
        sys.exit("You did not insert the coorect game index")

def get_game():
    gamenumber = input("Here insert the number of the game that u want to play: ")
    return gamenumber



def rockpaperscissors_instructions():
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("Type rock, paper, or scissors. First to win a round takes it.")
    RockPaperScissor()

def RockPaperScissor():
    usersign = input("Choose between rock paper of scissors\nChoice: ").lower().strip()
    botsign = random.choice(["rock", "paper", "scissors"])
    if not validesign(usersign):
        sys.exit("You did not insert a correct Value")
    elif usersign == botsign:
        print("You Tied!")
    elif won(usersign,botsign):
        print("You Won! Congrats")
    else:
        print(f"Unfortunately You lost! the sign was {botsign}")
        tryagain = input("Do u wish to try again ? yes/no: ").strip().lower()
        if tryagain == "yes":
            RockPaperScissor()
        elif tryagain == "no":
            sys.exit("Thank you for playing!")
        else:
            sys.exit("Excited to see you again in the future!")

def validesign(n):
    signs = ["rock", "paper","scissors"]
    if n not in signs:
        return False
    else:
        return True

def won(user,bot):
    if (user == "paper" and bot == "rock") or (user == "rock" and bot == "scissors") or (user == "scissors" and bot == "paper"):
        return True
    else:
        return False

def numbergame_instructions():
    print("Rules: I'm thinking of a number between 1 and 100.")
    print("Guess it.")
    print("You have an 1 guess, so choose wisely.")
    numbergame()


def numbergame():
        usernumbers = input("Input a number between 1 and 100\nInput: ")
        try:
            usernumber = int(usernumbers)
        except ValueError:
            sys.exit("You did not insert a number")
        botnumber = random.randint(1,100)
        if not inrange(usernumber):
            sys.exit("Your Number is Not between 1 and 100")
        elif usernumber == botnumber:
            print("Congratulation! You officially beat the odds")
        else:
            print(f"Unfortunately You lost the correct number was {botnumber}")
            tryagain = input("Do u wish to try again ? yes/no: ").strip().lower()
            if tryagain == "yes":
                numbergame()
            elif tryagain == "no":
                sys.exit("Thank you for playing!")
            else:
                sys.exit("Excited to see you again in the future!")


def inrange(n):
    return 1 <= n <= 100



if __name__ == "__main__":
    main()

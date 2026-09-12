# Luca's Games

#### Video Demo: https://youtu.be/JBQ_OU2CcmY

#### Description:

This project is a small collection of two terminal games. When you run it you get
a welcome banner made with the art library, and then it asks which game you want
to play: Rock Paper Scissors, or the Mythical Number Guessing Game. You pick by
typing 1 or 2. If you type anything else the program exits and tells you that you
did not insert the correct game index.

After you pick, it prints the rules for that game and then starts it. If you win
or tie, it says so and the program ends. If you lose it asks if you want to try
again, and you can say no if you want to stop.

## project.py

main() is where the program starts. It prints the welcome banner, shows the two
options, and calls get_game() to find out what the player picked. Then it prints
a confirmation, and sends the player to the instructions for whichever game they
chose. If the number is not 1 or 2 it exits with an error message.

get_game() just asks the player which game they want and returns what they typed.

rockpaperscissors_instructions() prints the rules for Rock Paper Scissors and then
calls RockPaperScissor() to actually run the game. numbergame_instructions() does
the same thing for the number game.

RockPaperScissor() asks the player for their sign and picks a random one for the
computer. It uses validesign() to check the player typed something valid, and
exits if they didn't. If the two signs are the same it prints that you tied,
otherwise it uses won() to figure out if the player won or lost. If you lose it
shows you what the computer picked and asks if you want to play again.

numbergame() asks for a number and tries to turn it into an integer. If that
fails it exits and says you did not insert a number. Then it picks a random number
between 1 and 100 and uses inrange() to make sure your guess is actually in range.
If your number matches the random one you win, and if it doesn't it tells you what
the number was and asks if you want to try again.

won() takes the player's sign and the computer's sign and returns True if the
player won, otherwise False. validesign() takes what the player typed and returns
True if it is rock, paper or scissors. inrange() takes a number and returns True
if it is between 1 and 100.

## test_project.py

I test three functions: inrange(), won() and validesign(). For each one I wrote
asserts for a case that should be True and a case that should be False.

## requirements.txt

The only outside library I use is art, for the ASCII banners, so that is the only
thing listed. sys and random come with Python so they don't need to go there.

## Design choices

I pulled won(), validesign() and inrange() out into their own functions instead of
writing that logic inside the games. It makes the code cleaner and easier to read,
because each check has a name that says what it does instead of being a long if
statement in the middle of everything.

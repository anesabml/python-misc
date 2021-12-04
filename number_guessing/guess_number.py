import random
import os

score_list = []

def show_score():
    if len(score_list) <= 0:
        print "There is currently no high score, it's yours for the taking!"
    else:
        print "The current hight score is %d" % (min(score_list))

def start_game():
    random_number = int(random.randint(1, 10))
    print "Hello %s! Welcome to the game of guesses!" % (os.getenv("username"))
    wanna_play = raw_input("Would you like to play the guessing game? (Y/N)\n").upper()
    attempts = 0
    show_score()
    while wanna_play == "Y":
        try:
            guess = int(raw_input("Pick a number between 1 and 10\n"))
            if guess < 1 or guess > 10:
                raise ValueError("Please guess a number withing the given range")
            if guess == random_number:
                print "Nice one! you got it"
                attempts += 1
                score_list.append(attempts)
                print "It took you %d attempts" % (attempts)

                wanna_play = raw_input("Would you like to play again? (Y/N)\n").upper()
                attempts = 0
                show_score()
                random_number = int(random.randint(1, 10))
                continue
            elif guess < random_number:
                print "It's higher"
                attempts += 1
            else:
                print "It's lower"
                attempts += 1
        except ValueError as err:
            print "Oh no!, that is not a valid value. Try again..."
            print err
    else:
        print "See you next time"


if __name__ == "__main__":
    start_game()
from words import word_list
import random

def get_word():
    return random.choice(word_list).upper()

def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print "Let's play Hangman!"
    print display_hangman(tries)
    print word_completion
    print "\n"
    while not guessed and tries > 0:
        guess = raw_input("Please guess a letter or word: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print "You already guessed", guess
            elif guess not in word:
                print guess + "is not in the word!"
                guessed_letters.append(guess)
                tries -= 1
            else:
                print "Good job.", guess, "is in the word!"
                guessed_letters.append(guess)
                word_completion_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_completion_as_list[index] = guess
                word_completion = "".join(word_completion_as_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print "You already guessed the word!", guess
            elif guess != word:
                print guess, "is not the word!"
                guessed_words.append(guess)
                tries -= 1
            else:
                guessed = True
                word_completion = word
        else:
            print "Not a valid guess."

        print display_hangman(tries)
        print word_completion
        print "\n"
    
    if guessed:
        print "Congrats, you guessed the word, you win!"
    else:
        print "Sorry, you ran out of tries. The word was " + word + ". Maybe next time!"

def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]

def main():
    while True:
        word = get_word()
        play(word)
        if raw_input("Play Again? (Y/N) ").upper() == "N":
            break

if __name__ == "__main__":
    main()
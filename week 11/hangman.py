import random
import time
#David
#Connor
#Ciara
#Aaron
#Gabe
#
#There are currently several (12) problems with this program. Some are "Logic problems" and some are random.
#These problems can range from code, to typos, to strings/input errors.
#Add all of your names to this program as a comment before one of your uploads.
def choose_word():
    with open("week 11/wordlist.txt", "r") as file:
        word_list = file.read().split() #is it splitlines or split?...
    return random.choice(word_list)

def displayword(word, guessed_letters):
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    return display_word

def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6

    while tries > 0:
        display_word = displayword(word, guessed_letters)
        print(display_word)
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Tries left: {tries}")
        

        if display_word == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess == "word":
            print(f"Congratulations! You guessed the word: {word} correctly!")
            
        elif guess in word:
            guessed_letters.append(guess)
            
        else:
            guessed_letters.append(guess)
            tries -= 1
            if tries == 0:
                print("You're out of tries. The word was: " + word)
                print("You lost. The word was: " + word)
                break
   

print("Welcome to my Hangman Game!")
print("You have 6 tries to win the game!")
print("Good luck.")
time.sleep(3)
hangman()


#fixed line 1 removed choice()
#fixed typo line 2
#fixed file name and path line 13
#fixed function calling line 33(added word and guessed_letters)
#fixed line 15 removed +randoom word
#fixed line 22 removed giberish 
#Added letter to line 22
#changed to split on line 14
#changed ramdom word to word line 56
#changed -=2 to =-1 line 54
#changed >0 to ==0 line 55
#Changed incorrectly to correctly line 47
#moved line 59 to line 57

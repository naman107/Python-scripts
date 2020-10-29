#Not for words having dupicate characters!!
#create a list of words and import it here
#words are of same length

from words import words
import random

print("Let's play hangman! Guess the word and win. You have (7) attempts!!")

def generate_word():
    our_word = random.choice(words)
    return our_word.upper()

our_word = generate_word()

def play(word):
    attempts = 7
    blanks = '_'*attempts
    user_word = list(blanks)
    while True:
        ch = input('Enter a character -> ').upper()
        if(ch in word):
            index = word.index(ch)
            user_word[index] = ch
            global finalWord
            finalWord = ''.join([str(x) for x in user_word])
            print(finalWord)
            if (word == finalWord):
                print('You win')
                return
        else:
            attempts = attempts - 1
            print(f"{ch} Not present in word. Attempts left {attempts}")
            if(attempts == 0):
                print('You lost')
                return

print(our_word)
play(our_word)

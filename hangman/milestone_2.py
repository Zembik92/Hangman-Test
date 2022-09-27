#import a python module
import random
#Create a list of your favorite fruits
word_list = ["apple", "banana", "pineapple", "mango", "grapes"]
#Using the random module, randomly print one of your favorite fruit
word = random.choice(word_list) 
print(word)

# Task one, ask the user to input one letter
while True:
    guess = input("Enter a single letter: ")
    if len(guess) ==1 and guess.isalpha():
        break
    else:
        print("Invalid letter. Enter a single letter")

#Task two, check if letter is in chosen word
if guess in word:
    print("Good job!!", guess, "is correct")           
else:
    if guess not in word:
        print("Too Bad!!", guess, "is not correct. Try again")
           

#Task three, convert the guessed letter to lowercase and define a fuction
def check_guess(guess):
    guess_lower = guess.lower()
    if guess_lower in word:
        print("Good job!!", guess_lower, "is correct")
    else:
        if guess_lower not in word:
            print("Too Bad!!", guess_lower, "is not correct. Try again")  
                
def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) ==1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Enter a single letter")
    check_guess(guess)

ask_for_input()
      

    

           
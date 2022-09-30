#import a python module
import random
#Create a list of your favorite fruits
word_list = ["apple", "banana", "pineapple", "mango", "grapes"]
#Using the random module, randomly print one of your favorite fruit
word = random.choice(word_list) 
print(word)
'''
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
'''
#Task three, put it all together in a function and call the functions
#check if letter is in chosen word
def check_guess(guess):
    guess= guess.lower()
    if guess in word:
        print("Good job!!", guess, "is correct")
    else:
        if guess not in word:
            print("Too Bad!!", guess, "is not correct. Try again")  
#ask user to input a letter, check if its a single aphabet                
def ask_for_input():
    while True:
        guess = input("Enter a single letter: ")
        if len(guess) ==1 and guess.isalpha():
            break
        else:
            print("Invalid letter. Enter a single letter")
    check_guess(guess)

ask_for_input()


      

    

           
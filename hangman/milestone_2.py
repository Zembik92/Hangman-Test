#import a python module
import random
#Create a list of your favorite fruits
word_list = ["apple", "banana", "pineapple", "mango", "grapes"]
#Using the random module, randomly print one of your favorite fruit
word = random.choice(word_list) 
print(word)


def ask_for_input():
    while True:   
    #Using the input function, ask the user to input a letter
        guess = (input("Enter a single letter: ")).lower()
        def check_guess(guess):
            if len(guess) == 1 and guess.isalpha():
                if guess in word:
                    print("Good job!!", guess, "is correct")
                    
                else:
                    if guess not in word:
                        print("Too Bad!!", guess, "is not correct. Try again")
            else:
                print("Sorry not valid input")
        check_guess(guess)
        break   
ask_for_input()  
                
    
    

           
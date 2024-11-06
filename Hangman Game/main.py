from display import *
from art import hangman_art
import random

words = ("apple", "orange", "coconut", "grapes", "pineapple")



def main():
    print("\n\nWelcome to Hangman Game!!!\n")
    wrong_guesses = 0
    answer = random.choice(words)
    hint = ['_']*len(answer)
    
    is_running = True
    
    while is_running:
        display_man(wrong_guesses, hangman_art)
        print()
        print("HINT :")
        display_hint(hint)   
        guess = input("Guess a letter: ").lower()
        print("x"*40)
        
        if len(guess) > 1:
            print("\nInvalid Input!!!\n")
            continue
        
        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
                    print("\nYou Guessed Correctly.\n")
        else:
            print("***Wrong Guess. Try Again.***")
            print("x"*40)
            # This is the answer reveiled as hint.
            # rand_index = random.randint(0,len(answer))
            # hint[rand_index] = answer[rand_index]
            
            wrong_guesses += 1
            
            
        if '_' not in hint:
            print("****RESULT****")
            print("Congratulations!!!, you have WON the Game.")
            print(f"Number of wrong attempts: {wrong_guesses}")
            exit()
            
        if wrong_guesses == 6:
            break
        
    
    print(" _ "*30)
    print("****RESULT****")
    print("You lost Game.")
    print(f"Correct Answer is: {answer}")
                    

if __name__ == "__main__":
    main()
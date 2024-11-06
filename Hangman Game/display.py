def display_man(wrong_guesses, hangman_art):
    print("*"*9)
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("*"*9)

def display_hint(hint):
    print(" ".join(hint))
    print()

def display_answer(answer):
    pass
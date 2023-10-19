#!/usr/bin/env python

print("Welcome to quiz game!")

print('Hello, Welcome to my quiz game!')

answer = input('Are you ready to play the quiz?(yes/no):')
import random

def main():
    """Start a song genre guessing game."""
    print("Contoh lagu Genre Etnikkreatif!")

    etnikkreatif = [
        "hati Kama",
        "cindai",
        "tiga dara",
        ]

    x = random.choice(etnikkreatif)
    print(x)
    guess = None

    while x != guess:

        guess = str(input("Contoh lagu Genre Etnikkreatif!?"))
        
        if x == guess:
            print("You guessed {}. Congratulations you got it right!".format(guess))
            break
        else:
            print("You guessed {}. Unfortunately you got the wrong answer. Please try again!".format(guess))


print('Thankyou for playing this small quiz game')
print('bye')


main()
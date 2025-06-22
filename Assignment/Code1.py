'''Number Guessing Game:
Write a program that generates a random number between 1 and 10. Use a while loop to allow the user to keep
guessing the number until they get it right. Use an if-else condition inside the loop to give hints
if the guess is too high or too low.'''

import random

secret_num=random.randint(1,10)
guess=None
print('Guess a the correct number between 1 and 10')
while guess != secret_num:
    try:
        guess=int(input('Enter your guess: '))
        if guess >secret_num:
            print('Your guess is too high')
        elif guess < secret_num:
            print('Your guess is too low')
        else:
            print('Congratulations, you guessed the correct number')
    except ValueError:
        print('Enter a valid number')

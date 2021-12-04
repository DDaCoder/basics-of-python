## A Number Guessing Game ##

# importing the random module from python that can generate random values
import random

# setting the variable number to the value of a randomly generated number between 1 and 5
number = random.randint(1, 5)
# setting the variable guess to the value of user input converted to an integer
guess = int(input("Guess my secret number. It is a number between 1 and 5: "))

# while the guess is still == to guess
while guess == guess:
    # if the guess turns out to be the same as the number, a message will be printed and the loop will stop
    if guess == number:
        print("You got it! My secret number is", number)
        break
    # else if the guess does not turn out to equal the number, prompt the user to try again
    elif guess != number:
        guess = int(input("Try again: "))
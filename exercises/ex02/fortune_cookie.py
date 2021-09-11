"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730395734"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


random_integer: int = randint(1, 100)
print("Your fortune cookie says...")

if random_integer > 75:
    print("You have a secret admirer!")
else:
    if random_integer == 9:
        print("Run.")
    else:
        if random_integer < 50:
            print("The greatest risk is not taking one.")
        else: 
            print("You already know the answer to the questions lingering inside your head.")

print("Now, go spread positive vibes!")
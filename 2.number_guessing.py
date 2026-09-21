# Number Guessing

import random
number = random.randint(1,10)
guess = int(input("Guess a number: "))
if guess == number:
    print("You Win")
else:
    print("try again!")



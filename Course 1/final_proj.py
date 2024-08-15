import random
import time
print("Welcomer to the guessing game,I am going to choose a number between 1 and 100!")
time.sleep(1)
print("Choosing number!")
time.sleep(2)
guess = int(input("What is your guess?: "))
guess_count = 0
correct_number = int(random.randint(1,100))
while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong! You need to guess higher! What is your guess?: "))
    else:
        guess = int(input("Wrong! You need to guess lower! What is your guess?: "))
print(f"Congrats! The right answer was {correct_number}! It took you {guess_count} guesses until you got it right!")

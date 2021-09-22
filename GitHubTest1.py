#! python3
import random

secretNumber = random.randint(1,100)
i = 0
print('Try to guess the number! (Between 1 and 100)')
while True:
    i = i + 1
    guess = int(input())
    if guess == secretNumber:
        break
    elif guess < secretNumber:
        print('Low')
    else:
        print('High')
print('Correct in ' + str(i) + ' guesses!')
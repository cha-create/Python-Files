import random

guessestaken = 0
number = str(random.randint(1,20))
name = input('Hello, What is your name?\n')
print(name + ', I am thinking of a number. Can you guess it in six tries?')

for guessestaken in range(6):
    guess = str(input())
    if guess > number:
       print('your guess is too high.')
    if guess < number:
        print('your guess is too low.')
    if guess == number:
        break
if guess == number and guessestaken > 1:
    print('good job ' + name + ', you guessed it in ' + str(guessestaken + 1)  + ' tries!')
if guess == number and guessestaken <= 1:
    print('good job ' + name + ', you guessed it in ' + str(guessestaken + 1)  + ' try!')
if guess != number:
    print('Better luck next time.')


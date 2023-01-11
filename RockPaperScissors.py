import random 
import time

while True:
    print("Hello, My name is GIGACHAD. this is a game of rock paper scissors. If you don't know how to play, I cant help you.")
    print("rock, paper, or scissors?")
    P = input()
    rand = random.randint(1, 3)
    if rand == 1:
        C = 'rock'
    if rand == 2:
        C = 'paper'
    if rand == 3:
        C = 'scissors'
    print('Rock,')
    time.sleep(1)
    print('Paper,')
    time.sleep(1)
    print('Scissors,')
    time.sleep(1)
    print('Shoot!')
    if P == 'rock' and C == 'paper':
        win = 'n'
    if P == 'paper' and C == 'rock':
        win = 'y'
    if P == 'paper' and C == 'scissors':
        win = 'n'
    if P == 'scissors' and C == 'paper':
        win = 'y'
    if P == 'rock' and C == 'scissors':
        win = 'y'
    if P == 'scissors' and C == 'rock':
        win = 'n'
    if P == C:
        win = 't'
    if win == 'y':
        print('you won. the computer chose {}. Would you like to play again(yes or no)?'.format(C))
        playagain = input()
        if playagain== 'yes':
            pass
        if playagain == 'no':
            break
    if win == 'n':
        print('you lost. the computer chose {}. Would you like to play again(yes or no)?'.format(C))
        playagain = input().lower()
        if playagain == 'yes':
            pass
        if playagain == 'no':
            break
    if win == 't':
        print('its a tie. would you like to play again(yes or no)?')
        playagain = input().lower()
        if playagain == 'yes':
            pass
        if playagain == 'no':
            break
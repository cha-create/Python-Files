import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
correctnumber = num1+num2
print("What is: " + str(num1) + " plus " + str(num2) + " ?")
guessednumber = int(input())
if guessednumber == correctnumber:
    print("You guessed the number correctly.")
    
elif guessednumber != correctnumber:
    print("haha you lost nub")  
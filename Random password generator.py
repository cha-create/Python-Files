import random   
import sys
import time
password = []
MAX_PASS_LENGTH = 12
alphabet = 'qwertyuiopasdfghjklzxcvbnm'

print("Welome to the auto-password generator. Before we generate a password, we need to define some basic parameters.")
time.sleep(1)
print("Please enter password length(3-12):")
RX = input()
if int(RX) >= 3 and int(RX) <= 12 and type(RX) == str:
    passlen = RX
else:
    print("invalid password")
    sys.exit()
if int(RX) < 0:
    passlen = abs(RX)
print("would you like alternating case? Sidenote: your password length will automagically be set to 12(yes or no)")
RX2 = input()
print("Proscessing")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
if RX2.lower().startswith('y'):
    passlen = 12
for i in range(int(passlen)):
    x = random.randint(0, 25)
    password.append(alphabet[x])
if RX2.lower().startswith("y"):
    password[1] = password[1].upper()
    password[3] = password[3].upper()
    password[5] = password[5].upper()
    password[7] = password[7].upper()
    password[9] = password[9].upper()
    password[11] = password[11].upper()
print("Here is your password:")
print("".join(password))
sys.exit()
from colorama import Fore, Back, Style
import os
import sys
import time

start = ("Welcome to Hangman!")
start2 = start.center(156, "-")
print(Fore.RED + start2)

def first():
    while True:

        x = input("Guess the Letter!")
        if x in list:
            print("That is correct!, the letter", x, "is in the word!")
            os.system("cls")
            break
        else:
            print("Try again!")
            continue

list = ["H","O","U","S","E","h","o","u","s","e"]

print(" ")
name = input("Whats your name?: ")
print(" ")
print("Welcome", name, "i hope you enjoy my name, im stil pretty new to python :p")
print(" ")

start2 = input("Would you like to start?: ")

if start2 == "yes":
    first()
else:
    print("Okay then, bye!")
    time.sleep(5)
    sys.exit()

print("Now guess the other letters!")

while True:

    x1 = input("Guess the second letter!")
    if x1 in list:
        print("The letter", x1, "is also in the word!")
        os.system("cls")
        break
    else:
        print("Try again!")
        continue

print("Three more letters to go!")

while True:

    x2 = input("Start!")
    if x2 in list:
        print("I cant belive you guessed" + x2)
        os.system("cls")
        break
    else:
        print("Try again!")
        continue

print("Your getting close!")

while True:

    x3 = input("Start!")
    if x3 in list:
        print("Wow you are so good at this game!")
        os.system("cls")
        break
    else:
        print("Try again!")
        continue

print("Last one!")

while True:

    x4 = input("Start!")
    if x4 in list:
        print("You got it!")
        os.system("cls")
        break
    else:
        print("Try again!")
        continue


print("Congratulations you won!")
print("Bye now!")
time.sleep(5)
sys.exit()












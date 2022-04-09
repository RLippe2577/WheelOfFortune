from random import Random


import random

#This Function gets a random word from a text file
def getword():
    f = open(r'C:\\Projects\\WheelOfFortune\Words.txt', 'r')
    words = f.readlines()
    f.close
    word1 = random.choice(words)
    word = word1[:len(word1) - 1]
    return(word)

#This function gets a user's guess and checks if a solve is correct
def solve(answer):
    guess = input('Enter your guess ').lower()
    if guess == answer:
        print('1')
        return 1
    else:
        print('0')
        return 0

#This function returns a random value from the wheel
def spin():


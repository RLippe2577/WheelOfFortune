from random import Random


import random

#This Function gets a random word from a text file
def getword():
    f = open(r'C:\\Projects\\WheelOfFortune\Words.txt', 'r')
    words = f.readlines()
    f.close
    word1 = random.choice(words)
    word = word1[:len(word1) - 1]
    return word

#This function gets a user's guess and checks if a solve is correct
def solve(answer):
    guess = input('Enter your solve guess ').lower()
    if guess == answer:
        return 1
    else:
        return 0

#This function returns a random value from the wheel
def spin():
    wheel = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 'bankrupt']
    outcome = random.choice(wheel)
    return outcome

#This function is for when a participant wants to guess a consonant
def const(answer, current):
    x = 0
    count = 0
    vowels = ['a','e','i','o','u']
    guess = input('Enter your consonant guess ').lower()
    if guess in vowels:
        output = [-1, current]
        return output
    elif guess in current:
        output = [-2, current]
        return output
    elif guess not in answer:
        output = [0, current]
        return output
    else:
        while x < len(answer):
            if answer[x] == guess:
                current[x] = guess
                x = x + 1
                count = count + 1
            else:
                x = x + 1
        output = [count, current]
        return output

#This function is for when a participant wants to guess a consonant
def vowel(answer, current):
    x = 0
    count = 0
    vowels = ['a','e','i','o','u']
    guess = input('Enter your consonant guess ').lower()
    if guess not in vowels:
        output = [-1, current]
        return output
    elif guess in current:
        output = [-2, current]
        return output
    elif guess not in answer:
        output = [0, current]
        return output
    else:
        while x < len(answer):
            if answer[x] == guess:
                current[x] = guess
                x = x + 1
                count = count + 1
            else:
                x = x + 1
        output = [count, current]
        return output

#This function will be used for the first two rounds of the game, and utilized previous functions
def round():
    answer = getword()
    current = []
    for i in answer:
        current.append('_')
    print('Current Puzzle is ' + str(current))
    money = {'player1' : 0, 'player2' : 0, 'player3' : 0}
    round = 0
    players = ['player1','player2','player3']
    p = 2
    currentplayer = players[p]
    while round == 0:
        turn = 0
        if currentplayer == players[2]:
            currentplayer = players[0]
        else:
            p = p + 1
            currentplayer = players[p]
        print('Current turn is for ' + currentplayer + ', Who has ' + str(money[currentplayer]) + ' dollars, current solve is ' + str(current))  
        round = 1
    
round()
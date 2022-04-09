import random


#This Function gets a random word from a text file. It takes no inputs and returns a random word from Words.txt
def getword():
    f = open(r'C:\\Projects\\WheelOfFortune\Words.txt', 'r')
    words = f.readlines()
    f.close
    word1 = random.choice(words)
    word = word1[:len(word1) - 1]
    return word

#This function gets a user's guess and checks if a solve is correct. It takes the answer as input and returns a 1 or 0 for correct or wrong.
def solve(answer):
    guess = input('Enter your solve guess :').lower()
    if guess == answer:
        return 1
    else:
        return 0

#This function returns a random value from the wheel. It takes no input and returns a random wheel value
def wheel():
    wheel = [100, 150, 200, 250, 300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800, 850, 900, 'bankrupt']
    outcome = random.choice(wheel)
    return outcome

#This function is for when a participant wants to guess a consonant. It takes the answer and current solve, and returns count, or 1 or 3 error types, and the new current solve array in an array.
def const(answer, current):
    x = 0
    count = 0
    vowels = ['a','e','i','o','u']
    guess = input('Enter your consonant guess :').lower()
    if guess in vowels:
        output = [-1, current]
        return output
    elif guess in current:
        output = [-2, current]
        return output
    elif guess not in answer:
        output = [0, current]
        return output
    elif len(guess) > 1:
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

#This function is for when a participant wants to guess a vowel. It takes the answer and current solve, and returns count, or 1 or 3 error types, and the new current solve array in an array.
def vowel(answer, current):
    x = 0
    count = 0
    vowels = ['a','e','i','o','u']
    guess = input('Enter your vowel guess :').lower()
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

#This function will be used for the first two rounds of the game, and utilizes the previous functions
#It will be run twice. It takes no input, and will return money dictionary to be used in the game function at the end
def round():
    answer = getword()
    #print(answer) #For testing purposes, uncomment to cheat as player1
    current = []
    for i in answer:
        current.append('_')
    print('Current Puzzle is ' + str(current)) #This tells the players how long the puzzle is
    money = {'player1' : 0, 'player2' : 0, 'player3' : 0}
    round = 0
    players = ['player1','player2','player3','extra'] #The extra slot in the array allows me to check if I've gone out of index and cycle to player 1
    p = -1
    while round == 0: #player cycling after each turn
        p = p + 1
        currentplayer = players[p]
        turn = 0
        if currentplayer == players[3]:
            currentplayer = players[0]
            p = 0
        while turn == 0: 
            print('Current turn is for ' + currentplayer + ', Who has ' + str(money[currentplayer]) + ' dollars, current solve is ' + str(current)) #turn information
            choice = input('please enter spin, vowel, or solve :').lower()
            options = ['vowel','spin','solve']
            if choice not in options:
                print('invalid input try again')
            elif choice == 'solve':
                correct = solve(answer)
                if correct == 1:
                    print('You got it! this round it over, answer was ' + answer)
                    turn = turn + 1
                    round = round + 1
                else:
                    print('That was not it, next player')
                    turn = turn + 1
            elif choice == 'vowel':
                if money[currentplayer] < 250:
                    print('Vowels cost $250, you do not have enough money, please solve or spin')
                else:
                    money[currentplayer] = money[currentplayer] - 250
                    output = vowel(answer, current)
                    if output[0] == -1:
                        print('That is not a vowel, you lose your $250 and a turn')
                        turn = turn + 1
                    elif output[0] == -2:
                        print('That vowel was already in the solution, you lose your turn and $250')
                        turn = turn + 1
                    elif output[0] == 0:
                        print('Sorry, none of those on the board, next player')
                        turn = turn + 1
                    else:
                        current = output[1]
                        print('Correct! there are ' + str(output[0]) + ' of those, you get another turn')
            else:
                spin = wheel()
                if spin == 'bankrupt':
                    print('Sorry, your spin was bankruptcy, you lose all money this round, and your turn')
                    money[currentplayer] = 0
                    turn = turn + 1
                else:
                    print('your spin was ' + str(spin))
                    output = const(answer, current,)
                    if output[0] == -1:
                        print('That is a vowel, you must buy those. you lose your turn')
                        turn = turn + 1
                    elif output[0] == -2:
                        print('That letter was already in the solution, you lose your turn ')
                        turn = turn + 1
                    elif output[0] == 0:
                        print('Sorry, none of those on the board, next player')
                        turn = turn + 1
                    else:
                        current = output[1]
                        winnings = output[0] * spin
                        money[currentplayer] = money[currentplayer] + (output[0] * spin)
                        print('Correct! there are ' + str(output[0]) + ' of those, you get another turn, and you won ' + str(winnings))
                        if '_' not in current:
                            print('That was the last letter, the round is over!') 
                            turn = turn + 1
                            round = round + 1
    return money

def checkletter(p, answer, current):
    x = 0
    while x < len(answer):
        if answer[x] == p:
            current[x] = p
            x = x + 1
        else: 
            x = x + 1
    return current

def validletter(letter):
    consonants = ['b','c','d','f','g','h','j','k','p','m','q','v,','w','x','y','z'] #to check input 
    validinput = 0
    while validinput == 0:
        if letter in consonants:
            validinput = 1
        else:
            print('That letter is in rstle, or is not valid, please try again')
            letter = input('please enter a consonant :').lower()

def validvowel(vowel):
    vowels = ['a','i','o','u'] #to check input 
    validinput = 0
    while validinput == 0:
        if vowel in vowels:
            validinput = 1
        else:
            print('That letter is in rstle, or is not valid, please try again')
            vowel = input('please enter a consonant :').lower()

def finalround():
    answer = getword()
    #print(answer) #Testing print. Uncomment to cheat
    current = []
    for i in answer:
        current.append('_')
    current = checkletter('r', answer, current) #RSTLNE 
    current = checkletter('s', answer, current)
    current = checkletter('t', answer, current)
    current = checkletter('l', answer, current)
    current = checkletter('n', answer, current)
    current = checkletter('e', answer, current)
    print('current board after RSTLNE is ' + str(current))
    letter = input('please enter a consonant :').lower()
    validletter(letter)
    current = checkletter(letter, answer, current)
    letter = input('please enter a consonant :').lower()
    validletter(letter)
    current = checkletter(letter, answer, current)
    letter = input('please enter a consonant :').lower()
    validletter(letter)
    current = checkletter(letter, answer, current)
    vowel = input('please enter a vowel :').lower()
    validvowel(vowel)
    current = checkletter(vowel, answer, current)
    print(str(current))
    print('You have one guess to solve this, good luck')
    correct = solve(answer)
    if correct == 1:
        print('Congradulations!!!! You win $10,000!!!!!')
        return 10000
    else:
        print('We are sorry but that was not it. the answer was ' + answer)
        print('You still win everything you won in rounds 1 and 2')
        return 0

def wheeloffortune():
    print('Welcome to wheel of fortune! I am your host Ryan, and we will soon be starting our first 3 player round')
    money1 = round()
    print('That was round one, current money totals are:')
    print(money1)
    print('We now begin round 2!')
    money2 = round()
    player1 = money1['player1'] + money2['player1']
    player2 = money1['player2'] + money2['player2']
    player3 = money1['player3'] + money2['player3']
    finalmoney = {'player1':player1,'player2':player2,'player3':player3}
    print('Totals after round2 are')
    print(finalmoney)
    winnings = max(player1, player2, player3)
    keys = list(finalmoney.keys())
    values = list(finalmoney.values())
    position = values.index(winnings)
    winner = keys[position]
    print('The winner is : ' + winner + '!!! Congradulations!! You made it to the final round, you have won ' + str(winnings) + ' so far')
    newmoney = finalround()
    final = newmoney + winnings
    print('Congradulations ' + winner + ', you have won $' + str(final) )


wheeloffortune()
    
    
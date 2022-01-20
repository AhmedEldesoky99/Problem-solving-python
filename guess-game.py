from random import shuffle

#function to shuffle list
def shuffle_list(myList):
    shuffle(myList)
    return myList

#function to take user guess
def user_guess():
    guess = ' '
    while guess not in [ '0' , '1' , '2']:
        guess = input('Guess where is the Ball : ')
        
    return int(guess)

#function to check the user answer
def check_answer(myList, guess):
    if myList[guess] == '0':
        print('correct!')
    else:
        print(myList)
        print('Try again good luck')

myList = [ ' ', '0', ' ']
shuffle_list(myList)
guess = user_guess()
check_answer(myList,guess)
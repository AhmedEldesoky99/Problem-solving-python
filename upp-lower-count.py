"""
Write a Python function that accepts a string and calculates the number of upper case letters and lower case letters.
"""

from curses.ascii import islower, isupper


def upp_low(sentance : str):
    lower = 0
    upper = 0
    for letter in sentance:
        if islower(letter):
            lower+= 1
        elif isupper(letter):
            upper+= 1
        else:
            pass

    print ('lower chars = {}\nupper chars = {}'.format(lower,upper))


upp_low('Hello Mr. Rogers, how are you this fine Tuesday?')

#another solution using dictionary
def upp_low2(sentance : str):
    d = {'upper': 0, 'lower': 0}

    for letter in sentance:
        if islower(letter):
            d['lower']+= 1
        elif isupper(letter):
            d['upper']+= 1
        else:
            pass

    print (f'lower chars = {d["lower"]}\nupper chars = {d["lower"]}')

upp_low2('Hello Mr. Rogers, how are you this fine Tuesday?')
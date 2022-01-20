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

    print ('lower chars = {}\nupper chars = {}'.format(lower,upper))


upp_low('Hello Mr. Rogers, how are you this fine Tuesday?')
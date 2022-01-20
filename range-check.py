from cgitb import reset


"""
Write a function that checks whether a number is in a given range (inclusive of high and low)
"""

def ran_check(num, min, max):
    return num >= min or num <= max

result = ran_check(3,1,10)
print (result)
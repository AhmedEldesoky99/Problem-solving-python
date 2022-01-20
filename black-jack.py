"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
 If their sum exceeds 21 *and* there's an eleven, reduce the total sum by 10. Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
    blackjack(5,6,7) --> 18
    blackjack(9,9,9) --> 'BUST'
    blackjack(9,9,11) --> 19
"""

from unittest import result


def blackjack(a,b,c):
    sumNums = sum((a,b,c))
    myList = [a,b,c]
    flag = False
    
    for num in myList:
        if num == 11:
            flag = True
    
    if sumNums <= 21:
        return sumNums
    elif sumNums > 21 and flag == True:
        return sumNums - 10 
    else:
        return 'bust'


result = blackjack(9,9,11)
print(result)


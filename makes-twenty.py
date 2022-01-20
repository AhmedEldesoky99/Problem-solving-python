"""
MAKES TWENTY: Given two integers, return True if the sum of the integers is 20 
*or* if one of the integers is 20. If not, return False
"""

def makes_twenty(num1, num2):
    if sum((num1,num2)) == 20 :
        return True
    elif num1 == 20 or num2 == 20:
        return True
    else:
        return False

#another sol
def makes_twenty2(n1, n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20



result = makes_twenty2(12,20)
print(result)

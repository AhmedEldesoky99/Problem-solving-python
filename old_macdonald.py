"""
OLD MACDONALD: Write a function that capitalizes the first and fourth letters of a name

from ntpath import join
import this
"""

def old_macdonald(name: str):

    myList = [letter for letter in name]
    myList[0] = myList[0].upper()
    myList[3] = myList[3].upper()

    result = "".join(myList)
   
    print(result)
        
#another solution 
def old_macdonald2(name: str):

    first_part = name[:3]
    second_part = name[3:]

    return first_part.capitalize() + second_part.capitalize()




result = old_macdonald2('macdonald')
print(result)
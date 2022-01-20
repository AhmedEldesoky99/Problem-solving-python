"""
FIND 33: 

Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.
"""

def has_33 (myList: list):

     for i in range(0 , len(myList)-1 ):
         if myList[i] == 3 and myList[i+1] == 3:
            return True
         
     return False
#another solution
def hass_33 (myList: list):

     for i in range(0 , len(myList)-1 ):
         if myList[i, i+1] == [3,3]:
            return True
         
     return False



result = has_33([3,3,2,3])
print (result)
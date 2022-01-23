"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)**

    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example : "The quick brown fox jumps over the lazy dog"

Hint: You may want to use .replace() method to get rid of spaces.
"""
import string

def is_pangram(strr: str, alphapet = string.ascii_lowercase):
    #create a set of alphapet
    alphapet_set = set(alphapet)
    #remove spaces form string
    strr = strr.replace(' ', '')
    #transform to lowercase
    strr = strr.lower()
    #create a set for strr letter
    strr_set = set()
    for letter in strr:
        if letter.isalpha():
            strr_set.add(letter)
    #compare two sets
    return strr_set == alphapet_set

    
reuslt = is_pangram("Pack my box with five dozen liquor jugs. - Mark Dunn")
print(reuslt)


#another solution
def is_pangram2(strr: str, alphapet = string.ascii_lowercase):
    #set1 to store my sentance
    set1 = set()
    for letter in strr:
        if(letter.isalpha()):
            set1.add(letter.lower())
        
   

    #set2 to store alphapet
    set2 = set()
    for letter in alphapet:
        set2.add(letter)

   
    return set1 == set2
    
    
reuslt = is_pangram2("Pack my box with five dozen liquor jugs. - Mark Dunn")
print(reuslt)




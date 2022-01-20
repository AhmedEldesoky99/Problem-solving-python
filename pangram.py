"""
Write a Python function to check whether a string is pangram or not. (Assume the string passed in does not have any punctuation)**

    Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
    For example : "The quick brown fox jumps over the lazy dog"

Hint: You may want to use .replace() method to get rid of spaces.
"""
import string

def is_pangram(strr: str, alphapet = string.ascii_lowercase):
    #set1 to store my sentance
    set1 = set()
    for letter in strr:
        if(letter.isalpha()):
            set1.add(letter.lower())
        
    print(set1)

    #set2 to store alphapet
    set2 = set()
    for letter in alphapet:
        set2.add(letter)

    print(set2)
    return set1 == set2
    
    

reuslt = is_pangram("Pack my box with five dozen liquor jugs. - Mark Dunn")
print(reuslt)




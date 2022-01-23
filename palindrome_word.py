"""
Write a Python function that checks whether a word or phrase is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
"""
def plindrome_word(s:str):
    #remove spaces
    s = s.replace(' ', '')
    return s == s[::-1]

result = plindrome_word("nurses run")
print(result)


#another solution
def plindrome_word2(s: str):
    sReverse = s[::-1]
    list1 = [letter for letter in s ]
    list2 = [letter for letter in sReverse]
    list1.remove(' ')
    list2.remove(' ')
  
    return list1 == list2

#plindrome_word2("nurses run")
result = plindrome_word("nurses run")
print(result)

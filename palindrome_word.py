"""
Write a Python function that checks whether a word or phrase is palindrome or not.
Note: A palindrome is word, phrase, or sequence that reads the same backward as forward,
e.g., madam,kayak,racecar, or a phrase "nurses run". Hint: You may want to check out the .replace() method in a string to help out with dealing with spaces. Also google search how to reverse a string in Python, there are some clever ways to do it with slicing notation.
"""


def plindrome_word(word: str):
    wordReverse = word[::-1]
    list1 = [letter for letter in word ]
    list2 = [letter for letter in wordReverse]
    list1.remove(' ')
    list2.remove(' ')
    print(list1)
    return list1 == list2

#plindrome_word("nurses run")
result = plindrome_word("nurses run")
print(result)

"""
SPY GAME: Write a function that takes in a list of integers and returns True if it contains 007 in order

     spy_game([1,2,4,0,0,7,5]) --> True
     spy_game([1,0,2,4,0,5,7]) --> True
     spy_game([1,7,2,0,4,5,0]) --> False
"""



import re


def spy_game(myList: list):
     
     result = []

     for num in myList:
          if num == 0 or num == 7:
               result.append(num)

     return result == [0, 0, 7]


print(spy_game([1,7,2,0,4,5,0])) 
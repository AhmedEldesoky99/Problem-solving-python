"""
PAPER DOLL: Given a string, return a string where for every character in the original there are three characters
    paper_doll('Hello') --> 'HHHeeellllllooo'
    paper_doll('Mississippi') --> 'MMMiiissssssiiippppppiii'
"""
from cgitb import reset


def paper_doll(string:str):
    myList = [ letter for letter in string]
    newList= []
    for letter in myList:
        for i in range(4):
            newList.append(letter)

    print("".join(newList))

#another solution
def paper_doll2(string: str):
    result = ''
    for char in string:
        result += char * 3

    print(result)

paper_doll2('hello')

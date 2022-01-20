
"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.**

    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]
"""

def unique_list(lst:list):
    myset = set()
    mylist = []

    for item in lst:
        myset.add(item)

    for item in myset:
        mylist.append(item)
    
    print(mylist)


unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
    

    
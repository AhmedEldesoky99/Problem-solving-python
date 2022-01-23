
"""
Write a Python function that takes a list and returns a new list with unique elements of the first list.**

    Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
    Unique List : [1, 2, 3, 4, 5]
"""

def unique_list(lst:list):
   return list(set(lst))


result = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(result)


#another solution 
def unique_list(lst:list):
    seen_number = []
    for num in lst:
        if num not in seen_number:
            seen_number.append(num)

    return seen_number

result = unique_list([1,1,1,1,2,2,3,3,3,3,4,5])
print(result)
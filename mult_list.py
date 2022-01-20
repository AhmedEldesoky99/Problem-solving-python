"""
Write a Python function to multiply all the numbers in a list.**

    Sample List : [1, 2, 3, -4]
    Expected Output : -24
"""
def mult_list(lst: list):
    mult = 1
    for num in lst:
        mult*= num

    print(mult)

mult_list([1, 2, 3, -4]) 
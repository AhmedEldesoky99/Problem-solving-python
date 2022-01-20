"""
write a function that returns the lesser of two given numbers *if* both numbers are even,
but returns the greater if one or both numbers are odd
"""
def even_less_odd_greater(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        if num1 > num2:
            result =  num2
        else:
            result = num1
    else:
        if num1 > num2:
            result = num1
        else:
            result = num2
    return result

#another sol
def even_less_odd_greater2(num1, num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1, num2)
    else:
        return max(num1, num2)

print(even_less_odd_greater(2,5))
print(even_less_odd_greater2(2,5))

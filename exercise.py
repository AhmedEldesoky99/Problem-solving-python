#this program split nums to odd , even
"""
start = int(input('Enter Start = '))
end = int(input('Enter End = '))

myList = [ num for num in range(start,end)]

odd = []
even = []

for num in myList:
    if( num % 2 == 0):
        even.append(num)
    else:
        odd.append(num)

print('Odd numbers = {}'.format(odd))
print('Even numbers = {}'.format(even))

"""
####################################################
#create a list of all numbers between 1 and 50 that are divisible by 3
"""
nums = [ num for num in range(1, 50) if num % 3 ==0]

print(nums)
"""


#####################################################################
"""
st = 'Print every word in this sentence that has an even number of letters'

st = st.split()

for word in st:
    if(len(word) % 2 == 0):
        print(f'{word} => even')
    else:
        print(f'{word} => odd')
     

"""
#################################################################
"""
#this program print words that start with letter s
str1 = 'Print only the words that start with s in this sentence'
str1 = str1.split()


for word in str1:
    if(word[0] == 's'):
        print(word)
"""
########################################################################
"""
for num in range(1,100):
    if num % 3 == 0  and  num % 5 == 0:
        print('fizzBuzz')
    if num % 3 == 0:
        print('fizz')
    elif num % 5 ==0:
        print('Buzz')
    else:
        print(num)

"""

#########################################################################
"""
st = 'Create a list of the first letters of every word in this string'

list = [ letter[0] for letter in st.split()]

print(list)    
"""

myList = [1, 2, 3]

help(myList.extend)
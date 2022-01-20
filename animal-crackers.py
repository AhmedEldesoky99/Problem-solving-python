"""
ANIMAL CRACKERS: Write a function takes a two-word string and returns True if both words begin with same letter
    animal_crackers('Levelheaded Llama') --> True
    animal_crackers('Crazy Kangaroo') --> False
"""
def animal_cracker(myAnimal: str):
    myStr = myAnimal.split()
    if(myStr[0][0] == myStr[1][0]):
        return True
    else:
        return False
    
#another solution
def animal_cracker2(myAnimal: str):
    myStr = myAnimal.lower().split()
    
    return myStr[0][0] == myStr[1][0]

animal = animal_cracker2('Levelheaded Llama')
print(animal)


def word_even_odd(string: str):
    st = string.split()

    for word in st:
        if(len(word) % 2 == 0):
            print(f'{word} => even')
        else:
            print(f'{word} => odd')


st = 'Print every word in this sentence that has an even number of letters'
word_even_odd(st)
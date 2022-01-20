"""
COUNT PRIMES: Write a function that returns the *number* of prime numbers that exist up to and including a given number
    count_primes(100) --> 25

By convention, 0 and 1 are not prime.
"""
def count_primes(n):
    counter = 0
    
    for num in range(n):# 1 2 3 4 5 6 7  8 9
        if num <= 1:
            continue
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            counter += 1

    return counter

result = count_primes(10)
print(f"Count prime = {result}")

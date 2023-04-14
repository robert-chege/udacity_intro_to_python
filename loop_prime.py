"""
Question: Write code to check if the numbers provided in the list check_prime are prime numbers.
For each number, if the number is prime, the code should print that the number is a prime number.
If the number is NOT a prime number, it should print that the number is not a prime number,
and also print a factor of that number besides 1 and the number itself.
"""

check_prime = [26, 39, 51, 53, 57, 79, 85]

# iterate through the check_prime list
for num in check_prime:

# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):

# number is not prime if modulo is 0
        if (num % i) == 0:
            print(f"{num} is NOT a prime number, because {i} is a factor of {num}")
            break

# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print(f"{num} IS a prime number")
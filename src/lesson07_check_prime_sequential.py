# SuperFastPython.com
# check if large numbers are prime
from math import sqrt
from math import floor

# returns True if prime, False otherwise
def is_prime(number):
    # 1 is a special case of not prime
    if number <= 1:
        return False
    # 2 is a special case of a prime
    if number == 2:
        return True
    # check if the number divides by 2 with no remainder
    if number % 2 == 0:
        return False
    # limit divisors to sqrt(n)+1 so range will reach it
    limit = floor(sqrt(number)) + 1
    # check all odd numbers in range
    for i in range(3, limit, 2):
        # check if number is divisible with no remainder
        if number % i == 0:
            # number is divisible and is not a prime
            return False
    # number is probably prime
    return True

# check if a series of numbers are prime or not
def check_numbers_are_prime(numbers):
    # check each number in turn
    for number in numbers:
        if is_prime(number):
            print(f'{number} is prime')

# protect the entry point
if __name__ == '__main__':
    # define some numbers to check
    NUMS = [17977, 10619863, 106198, 6620830889,
        80630964769, 228204732751, 1171432692373,
        1398341745571, 10963707205259, 15285151248481,
        99999199999, 304250263527209, 30425026352720,
        10657331232548839, 10657331232548830,
        44560482149, 1746860020068409]
    # check whether each number is a prime
    check_numbers_are_prime(NUMS)

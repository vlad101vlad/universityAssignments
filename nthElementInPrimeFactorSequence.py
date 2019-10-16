'''
[14] Determine the n-th element of the sequence 1,2,3,2,2,5,2,2,3,3,3,7,2,2,3,3,3,...
obtained from the sequence of natural numbers by replacing composed numbers with their prime divisors,
each divisor d being written d times, without memorizing the elements of the sequence
'''
from math import sqrt


def is_prime(number):
    '''Computes whether a number is prime or not

    Computes whether a number is prime or not

    :param n: Natural number
    :return: 0 - if the number is composed // 1 - if the number is prime
    '''
    if number == 2:
        return 1
    if number % 2 == 0:
        return 0

    for iterator in range(3, int(sqrt(number)) + 1, 2):
        if number % iterator == 0:
            return 0
    return 1


def get_nth_element_in_divisors_sequence(nth_element):
    if nth_element <= 3:
        return nth_element
    else:
        position_in_sequence = 3 #keeps the position in the sequence
        current_number_to_find_divisors = 4 # the number of which we compute the divisors

        while 1 == 1:
            for prime_divisor in range(2, current_number_to_find_divisors):
                if is_prime(prime_divisor) == 1:                       #j has to be a prime divisor, so it makes sense to verify if it is the case
                    if is_prime(current_number_to_find_divisors) == 1:               #if we have a prime number, we don't have to search for it's divisors, we just increase the ocunter
                        position_in_sequence += 1
                        if position_in_sequence == nth_element:                  #also we have to check if we reach the limit// be it the case we return the function
                            return current_number_to_find_divisors
                        break                               #we have to exit the loop because we will have a new number
                    else:

                        copy_current_number_to_find_divisors = current_number_to_find_divisors      # Since we will work with the number's value , we need an aux , otherwise the above 'for' with loop forever
                        if copy_current_number_to_find_divisors % prime_divisor == 0:                     # We found a prime divisor for our number
                            while copy_current_number_to_find_divisors % prime_divisor == 0 and copy_current_number_to_find_divisors> 0:  # We eliminate the powers of the prime divisor
                                copy_current_number_to_find_divisors /= prime_divisor

                            for iterator in range (0, prime_divisor):   # We should print the prime divisors j times
                                position_in_sequence += 1        # We add 1 more number to the sequence
                                if position_in_sequence == nth_element:    # If the counter is equal to the n-th number in the sequence
                                    return prime_divisor        # We return the prime divisor
            current_number_to_find_divisors += 1




if __name__ == '__main__':
    number = int(input("number="))
    print("The {0}-th number of the sequence is: {1} ".format(number, get_nth_element_in_divisors_sequence(number)))
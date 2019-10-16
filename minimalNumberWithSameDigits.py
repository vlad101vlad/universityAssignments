# [3] For a given natural number n find the minimal
# natural number m formed with the same digits. (e.g. n=3658, m=3568).

'''
    In order to solve this problem I propose a frequency array which stores how many times each digit is present in the initial number

    With ease, we can form the minimal number by looping through the array and printing each digit which has a frequency >0. After each
    print, we decrease the frequency of every digit by 1 until it is 0.

    We have a special case with 0 which cannot be the first number. In order to solve the problem correctly , we search for the first
    number which is != 0 and print it on the screen. Then , we print all the 0's.
    After that , the aforementioned algorithm applies .
'''

def create_digit_frequency_array(number):
    '''Populates the frequency array

    It populates the frequency array: we have 10 digits (0-9) which will have a frequency of 0 initially.
    The function will loop through the digits of <n> and update the frequency of them accordingly.


    :param n: natural number
    '''

    for iterator in range(0,10):
        array.append(0)

    while number > 0 :
        array[int(number%10)] += 1
        number //= 10


def print_the_min_number(number):
    '''Prints the minimal natural number which is formed with the digits of the inputed number.

    We loop through the already populated array(we start from 1 because a number can't start with 0).
    The first thing we check is whether we have 0 digits of not.
        -> If we have , we search the first non 0 digit and print it on the screen. After that we print all the 0 digits.
    After that , we print all the other digits.

    '''
    print("The minimal natural number formed with the digits of {0} is: ".format(number),end=" ")
    for iterator in range(0,10):
        if array[0] > 0:
            for digit in range(1,10):
                if(array[digit] > 0):
                    print(digit, end="")
                    array[digit] -= 1
                    break

        while array[iterator] > 0:
            print(iterator,end="")
            array[iterator] -= 1


if __name__ == '__main__':

    number = int(input("n = "))      # Inputs n

    if number == 0:
        print("0")
    else:
        array = []                  # We declare the frequency array
        create_digit_frequency_array(number)           # Populates the array with the digits of n
        print_the_min_number(number)      # We print the solution (the minimal number) on the screen





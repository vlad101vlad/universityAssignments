"""
Implement a menu-driven console application that provides the following functionalities:
1. Read a list of complex numbers (in z = a + bi form) from the console.
2. Display the entire list of numbers on the console.
3. Display on the console the longest sequence that observes a given property. Each student will receive 2 of
the properties from the list provided below.
4. Exit the application.
The source code will include:
a. Specifications for the functions related to point 3 above.
b. 10 suitable complex numbers already available at program startup.
"""


import time
from collections import OrderedDict


def convert_string_to_complex_number(complex_string):
    """
    This function transforms the string input of the user who enters a complex number into a pair which held the vlaues
    of the real and imaginary part
    :param complex_string:  A complex number in the form of a string (z = a + bi)
    :return: A complex number in the form of a pair [a,b] where a - the real part and b- the imaginary part
    """

    complex_values = []
    imaginary_part = 0
    complex_string = "  " + complex_string + "   "

    if 'i' in complex_string:
        imaginary_part = 1

    sign = 1
    position = 0
    while position < len(complex_string):
        if complex_string[position] == '+':
            sign = 1

        if complex_string[position] == '-':
            sign = -1

        if complex_string[position].isdigit():
            new_number = ""
            while complex_string[position].isdigit():
                new_number = new_number + complex_string[position]
                position += 1

            complex_values.append(int(new_number)*sign)
            position -= 1

        position += 1

    if imaginary_part == 0 and len(complex_values) == 1:
        complex_values.append(0)
    if imaginary_part == 1 and len(complex_values) == 1:
        complex_string.split()
        for iterator in range(0, len(complex_string)):
            if complex_string[iterator] == 'i':
                if complex_string[iterator-1] == '-':
                    complex_values.append(-1)
                elif complex_string[iterator-1] == '+':
                    complex_values.append(+1)
                else:
                    complex_values.append(complex_values[0])
                    complex_values[0] = 0
    if imaginary_part == 1 and len(complex_values) == 0:
        if '-' in complex_string:
            complex_values = [0, -1]
        else:
            complex_values = [0, 1]

    return complex_values


def create_complex_number(complex_number):
    return [0, 0]


def set_imaginary_value(complex_number, imaginary_value):
    complex_number[1] = imaginary_value
    return complex_number


def set_real_value(complex_number, real_value):
    complex_number[0] = real_value
    return complex_number


def get_real_value(complex_number):
    return complex_number[0]


def get_imaginary_value(complex_number):
    return complex_number[1]


def read_complex_number(complex_number_list):
    complex_string = input()
    complex_number = convert_string_to_complex_number(complex_string)
    return complex_number


def read_complex_number_list(complex_number_list):
    """
    This functions reads from the user a list of complex numbers
    :param complex_number_list: A list of complex numbers
    :return: A list of complex numbers
    """
    # complex_number_list = []  # This can be changes if we want to add to the existing list or not

    how_many_numbers = int(input("How many complex numbers do you wish to enter?: "))
    for iterator in range(0, how_many_numbers):
        print("Number #{0}: ".format(iterator+1))
        complex_number_list.append(read_complex_number(complex_number_list))
    print("\n")
    print("You have read {0} complex number !\n".format(how_many_numbers))
    return complex_number_list


# def get_increasing_real_part_sequence(complex_number_list):
#     increasing_list = []
#     last_real_value = 'x'

# def get_increasing_real_part_sequence(complex_number_list):
#     increasing_list = []  # Stores the longest increasing sequence of real numbers
#     last_real_value = "x"    # Store the last value in the sequence of increasing numbers
#     current_increasing_list = []   # Stores the current sequence of increasing real numbers
#
#     for iterator in range(len(complex_number_list)):
#         complex_number = complex_number_list[iterator]
#
#         if last_real_value == 'x':
#             last_real_value = int(get_real_value(complex_number))
#             current_increasing_list.append(last_real_value)
#
#         if last_real_value < get_real_value(complex_number):
#             current_increasing_list.append(get_real_value(complex_number))
#             last_real_value = get_real_value(complex_number)
#
#             if iterator+1 == len(complex_number_list):
#                 if len(current_increasing_list) > len(increasing_list):
#                     increasing_list = current_increasing_list
#                     current_increasing_list = []
#                     last_real_value = get_real_value(complex_number)
#
#         else:
#             if len(current_increasing_list) > len(increasing_list):
#                 increasing_list = current_increasing_list
#                 current_increasing_list = []
#                 last_real_value = get_real_value(complex_number)
#             else:
#                 current_increasing_list = []
#                 last_real_value = get_real_value(complex_number)
#
#     return increasing_list

def get_increasing_real_part_sequence(complex_number_list):
    """
    This function iterates through a list of complex numbers and finds the longest sequence of complex numbers in which
    the real part of the number is strictly incearsing

    :param complex_number_list: A list with complex numbers
    :return: The list with the longest sequence of complex numbers which verify the give property
    """
    increasing_list = []    # Stores the longest increasing sequence of real numbers
    last_real_value = "x"    # Store the last value in the sequence of increasing numbers
    current_increasing_list = []   # Stores the current sequence of increasing real numbers

    for iterator in range(0, len(complex_number_list)):      # We search for every complex number in the list
        complex_number = complex_number_list[iterator]

        if last_real_value == 'x':               # We need the last value in order to compare two numbers
            last_real_value = int(get_real_value(complex_number))
            current_increasing_list.append(complex_number)

        if last_real_value < get_real_value(complex_number):  # If the current number is bigger than the last
            last_real_value = get_real_value(complex_number)
            current_increasing_list.append(complex_number)     # We append it to the current list

            if (iterator+1) == len(complex_number_list):
                if len(current_increasing_list) > len(increasing_list):
                    # If the current list is longer than the one we found before
                    increasing_list = current_increasing_list  # We update it
                    current_increasing_list = []

        else:   # When the current element isn't bigger then the last one
            if len(current_increasing_list) > len(increasing_list):    # If the current list is longer than the one we found before
                increasing_list = current_increasing_list              # We update it
                current_increasing_list = []                           # And we empty the current one
                last_real_value = int(get_real_value(complex_number))
                current_increasing_list.append(complex_number)
            else:
                last_real_value = int(get_real_value(complex_number))
                current_increasing_list = []
                current_increasing_list.append(complex_number)   # We do the same when we don't find a longer sequence

    return increasing_list


def get_digits_complex_number(complex_number):
    """
    This function receives a complex number and puts all the digits from its complex form in a sorted string

    :param complex_number: A complex number which will be broken into a string
    :return: A string which contains all the digits in the complex form of the argument number
    """
    string = "0"
    string = string + str(get_real_value(complex_number))
    string = string + str(get_imaginary_value(complex_number))
    string = "".join(sorted(string))
    string = "".join(OrderedDict.fromkeys(string))
    #print(string)
    return string


def check_if_digits_in_list(list, digits_string):
    for iterator in range(0, len(digits_string)):
        if digits_string[iterator] != '-' and (digits_string[iterator] not in list):
            return 0
    return 1


def get_numbers_written_with_same_digits_sequence(complex_number_list):
    """
    This function checks and returns a list of complex numbers which can be formed using the same digits
    :param complex_number_list: A list with complex numbers
    :return: A list with the longest sequence of complex numbers which can be formed with the same digits
    """
    maximum_lenght_same_digit_list = []
    current_same_digit_list = []
    current_digits_in_list = ""

    for iterator in range(len(complex_number_list)):
        number = complex_number_list[iterator]

        if current_digits_in_list == "":
            current_digits_in_list = get_digits_complex_number(number)
            current_same_digit_list.append(number)
        else:
            if check_if_digits_in_list(current_digits_in_list, get_digits_complex_number(number)):
                current_same_digit_list.append(number)

                if (iterator+1) == len(complex_number_list):
                    if len(current_same_digit_list) > len(maximum_lenght_same_digit_list):
                        maximum_lenght_same_digit_list = current_same_digit_list
                        current_same_digit_list = []
                        current_digits_in_list = get_digits_complex_number(number)
            else:
                if len(current_same_digit_list) > len(maximum_lenght_same_digit_list):
                    maximum_lenght_same_digit_list = current_same_digit_list
                    current_same_digit_list = []
                    current_digits_in_list = get_digits_complex_number(number)
                    current_same_digit_list.append(number)
                else:
                    current_same_digit_list = []
                    current_digits_in_list = get_digits_complex_number(number)
                    current_same_digit_list.append(number)

    return maximum_lenght_same_digit_list


def display_complex_number_list(complex_number_list):
    """
    This function iterates through the complex_list_numbers and prints every single element of it
    in the z = a + bi form
    """
    for complex_number in complex_number_list:
        if get_real_value(complex_number):
            print(get_real_value(complex_number), end="")
        if get_imaginary_value(complex_number) > 0:
            print("+", end="")
        if get_imaginary_value(complex_number):
            if get_imaginary_value(complex_number) == 1 or get_imaginary_value(complex_number) == -1:
                if get_imaginary_value(complex_number) == -1:
                    print("-", end="")
                print("i", end="")
            else:
                print(get_imaginary_value(complex_number), end="")
                print("i", end="")
        print(" ")


def menu():
    default_list = [[0, -1], [10, 1], [3, -2], [-23, -35], [3, 232], [-32, 26], [1, 2], [8, 0], [-1, -1], [4, 5]]

    while True:

        print("Welcome to the menu! Chose an action from below:\n"
              "1 -> Read a list of complex numbers (in z = a + bi form) from the console.\n"
              "2 -> Display the entire list of numbers on the console.\n"
              "3 -> Display on the console the longest sequence of complex numbers \n"
              "with a strictly increasing real part.\n"
              "4 -> Display on the console the longest sequence of complex numbers\n"
              " that can be written using the same base 10 digits\n"
              "x -> Exit \n")
        option_from_user = input("Enter your option: ")

        if option_from_user == 'x':
            print("You have exited the application !")
            break
        option_from_user = int(option_from_user)

        if option_from_user == 1:
            default_list = read_complex_number_list(default_list)
            time.sleep(5)

        if option_from_user == 2:
            #print(default_list)
            display_complex_number_list(default_list)
            print("These are the current complex numbers in the list\n")
            time.sleep(5)

        if option_from_user == 3:
            display_complex_number_list(get_increasing_real_part_sequence(default_list))
            print("This is the longest sequence with a strictly increasing real part\n")
            time.sleep(5)

        if option_from_user == 4:
            display_complex_number_list(get_numbers_written_with_same_digits_sequence(default_list))
            print("This is the longest sequence with complex numbers which can be written with the same digits")
            time.sleep(5)


if __name__ == '__main__':
    menu()
    #print(string_to_complex("21+10i"))
    #print(string_to_complex("-2i"))
    #print(get_digits_complex_number([2, -141221]))
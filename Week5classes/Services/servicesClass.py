import Domain.complexNumberClass as ComplexClass
import random
import time


class Services:
    def __init__(self):
        print("Multiple services can be used!\n")

    @staticmethod
    def add_ten_random_complex_numbers(list_of_complex_numbers):
        for iterator in range(0, 10):
            real_part = random.randint(-100, 100)
            imaginary_part = random.randint(-100, 100)
            complex_number = ComplexClass.ComplexNumber(real_part, imaginary_part)
            list_of_complex_numbers.append(complex_number.print_form)

    @staticmethod
    def add_complex_number_to_list(list_of_complex_numbers, real_part = None, imaginary_part = None):
        try:
            if real_part is None and imaginary_part is None:
                real_part = int(input("Enter the real part:~"))
                imaginary_part = int(input("Enter the imaginary part:~"))

            complex_number = ComplexClass.ComplexNumber(real_part, imaginary_part)
            list_of_complex_numbers.append(complex_number.print_form)
        except ValueError:
            print("The real and imaginary part have to be type:int\n")
            time.sleep(1)

    @staticmethod
    def filter_list_from_start_to_end_position(list, start_position = None, end_position = None):
        try:
            if start_position is None and end_position is None:
                start_position = int(input("Input pStart:~"))
                end_position = int(input("Input pEnd:~"))

            new_list = []
            for iterator in range(start_position, end_position + 1):
                new_list.append(list[iterator])

            list[:] = new_list
        except ValueError:
            print("The position values must be type: int\n")
            time.sleep(1)
        except IndexError:
            print("There are only {0} elements in the list".format(len(list)))
            time.sleep(1)

    @staticmethod
    def save_current_state(current_list, backup_list):
        backup_list.append(current_list[:])

    @staticmethod
    def undo_last_action(current_list, backup_list):
        previous_iteration = backup_list.pop()
        current_list[:] = previous_iteration[:]










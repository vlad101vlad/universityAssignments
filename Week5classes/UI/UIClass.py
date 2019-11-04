import Services.servicesClass as Service
import time
from test.tests import *


class Menu:
    #command = 0

    def __init__(self):
        self.command = "x"

    @property
    def command(self):
        return self.command

    @staticmethod
    def print_menu():
        print("Welcome to the menu! Chose what you want to do:\n"
              "1) Add a number to the list\n"
              "2) Show the list of numbers\n"
              "3) Filter the list so it contains only the numbers between a start position and an end position\n"
              "4) Undo last operation\n"
              "x) Exit the program.\n")

    @staticmethod
    def print_the_elements_of_list(list):
        print("The current elements in the list are: \n")
        for iterator in range(len(list)):
            print("Element #{0}: ".format(iterator+1), list[iterator])
        print("\n")
    #
    # @staticmethod
    # def print_elements_list_between_two_positions(list):
    #     try:
    #         start_position = int(input("Input pStart:~"))
    #         end_position = int(input("Input pEnd:~"))
    #
    #         for iterator in range(start_position, end_position + 1):
    #             print(list[iterator])
    #         print("\n")
    #     except ValueError:
    #         print("The position values must be type: int\n")
    #         time.sleep(1)

    def run_menu(self):
        service = Service.Services()
        test_all_functions()
        list_of_complex_numbers = []
        undo_list = []
        service.add_ten_random_complex_numbers(list_of_complex_numbers)

        while True:
            self.print_menu()
            self.command = input("Enter your option:~ ")

            if self.command == 'x':
                print("You have closed the application! \n")
                break

            if self.command == '4':
                if undo_list:
                    service.undo_last_action(list_of_complex_numbers, undo_list)
                else:
                    print("There aren't any actions to be undone!\n")
                    print("\n")
                    time.sleep(2)
                continue

            commands = {1: service.add_complex_number_to_list, 2: self.print_the_elements_of_list,
                        #3: self.print_elements_list_between_two_positions
                        3: service.filter_list_from_start_to_end_position}

            undo_commands = [1, 3]

            try:
                self.command = int(self.command)

                if self.command in undo_commands:
                    service.save_current_state(list_of_complex_numbers, undo_list)

                commands[self.command](list_of_complex_numbers)
            except KeyError:
                print("We don't have an action for this command\n")
                time.sleep(2)
            except ValueError:
                print("Commands must be type:int\n")
                time.sleep(2)




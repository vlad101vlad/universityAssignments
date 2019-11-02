import Modular_programming.UI_functions as UI
import Modular_programming.UI_menu_based as Menu
import sys

if __name__ == '__main__':
    #print("I'm in main")

    while True:
        print("Welcome to the application. Choose a menu:\n"
              "1. Command based\n"
              "2. Menu based\n"
              "x. Exist the application")

        command = input("Enter your option:~")
        print("\n")
        if command == 'x':
            sys.exit("You have closed the applicaton")

        try:
            command = int(command)
        except ValueError:
            print("Invalid value")
        except TypeError:
            print("Invalid type")

        if command == 1:
            UI.menu()
        if command == 2:
            Menu.menu()

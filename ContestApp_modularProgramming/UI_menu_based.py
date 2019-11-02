import Modular_programming.contest_functions as functions
import sys
import Modular_programming.UI_functions as UI
import Modular_programming.undo as UND
import time


def print_menu():
    print("Welcome to the menu! Chose an action :\n"
          "1: Add and insert menu\n"
          "2: Remove and replace menu\n"
          "3: Property menu\n"
          "4: Characteristics menu\n"
          "5: Undo the last action \n"
          "x: exists the application.")


def add_and_insert_menu(list_of_students):
    print("Welcome to add and insert menu! Chose and action:\n"
          "1: Add participant to the list\n"
          "2: Insert participant at a certain position\n"
          "m: Back to menu:\n"
          "x: Exist de application\n")

    action = input("Enter your option: ")

    if action == 'x':
        sys.exit("You have exited the application")
    if action == 'm':
        return

    action = int(action)
    p1_score = int(input("Enter the score for P1: "))
    p2_score = int(input("Enter the score for P2: "))
    p3_score = int(input("Enter the score for P3: "))

    if action == 2:
        postion = int(input("Enter the position to be inserted at: "))
        functions.insert_student_with_score_to_a_position_in_list(list_of_students, p1_score, p2_score,
                                                                  p3_score, postion)
        print("You have added a new participant to the list!\n")
    else:
        if action == 1:
            functions.add_student_to_list(list_of_students, p1_score, p2_score, p3_score)
            print("You have inserted a new participant to the list!\n")


def remove_and_replace_menu(list_of_students):
    print("Welcome to remove and replace menu! Chose and action:\n"
          "1: Remove the scores from a participant\n"
          "2: Remove the score from participant between two positions\n"
          "3: Remove the scores from participants with an average < = > then a given value"
          "4: Replace a participant's score to a certain problem\n"
          "m: Back to menu:\n"
          "x: Exist de application\n")

    action = input("Enter your command: ")

    if action == 'x':
        sys.exit("You have exited the application")

    if action == 'm':
        return
    action = int(action)

    if action == 1:
        position = int(input("Enter the postion to be removed: "))
        functions.remove_score_from_student(list_of_students, position)
        print("You have removed the score from the position ", position, "\n")
    if action == 2:
        start_position = int(input("Enter the start position to be removed: "))
        end_position = int(input("Enter the end postion to be removed: "))
        functions.remove_score_from_student(list_of_students, start_position, end_position)
        print("You have removed the score from the positions ", start_position, " to ", end_position, "\n")
    if action == 3:
        sign = input("Enter the sign. It can be <, = or >: ")
        value = float(input("Enter the value: "))
        functions.remove_score_from_student(list_of_students, sign, value)
        print("You have removed the score from the participant with a score ", sign, " than ", value, "\n")
    if action == 4:
        participant_postion = int(input("Enter the participant position: "))
        problem_index = int(input("Enter the problem number: "))
        new_score = int(input("Enter the new score: "))
        functions.replace_score_in_position(list_of_students, participant_postion, problem_index, new_score)
        print("You have replaced the score for the ", participant_postion, " participant at problem ",
              problem_index, " with the new score of ", new_score, "\n")


def property_menu(list_of_students):
    print("Welcome to property menu! Chose and action:\n"
          "1: Print the current participants in the list\n"
          "2: Print the participants sorted by their average score\n"
          "3: Print the participant with their average score < = > than a value\n"
          "m: Back to menu:\n"
          "x: Exist de application\n")

    action = input("Enter your command: ")

    if action == 'x':
        sys.exit("You have exited the application")

    if action == 'm':
        return

    action = int(action)

    if action == 1:
        UI.print_students_in_list(list_of_students)
    if action == 2:
        UI.print_students_in_list(list_of_students, "sorted")
    if action == 3:
        sign = input("Enter the sign. It can be < , = or >: ")
        value = float("Enter the value: ")
        UI.print_students_in_list(list_of_students, sign, value)


def characteristic_menu(list_of_students):
    print("Welcome to property menu! Chose and action:\n"
          "1: Compute the average of the average score for the participant between two positions\n"
          "2: Get the lowest average score of the participants between two positions\n"
          "3: Get the participants with the best n average scores\n"
          "4: Get the participants with the best n scores at a certain problem\n"
          "m: Back to menu:\n"
          "x: Exist de application\n")

    action = input("Enter your command: ")
    if action == 'x':
        sys.exit("You have exited the application")

    if action == 'm':
        return
    action = int(action)

    if action == 1:
        start_position = int(input("Enter the start position: "))
        end_position = int(input("Enter the end position: "))
        UI.print_average_score_between_two_positions(list_of_students, start_position, end_position)
    if action == 2:
        start_position = int(input("Enter the start position: "))
        end_position = int(input("Enter the end position: "))
        UI.print_minimum_average_score_between_two_positions(list_of_students, start_position, end_position)
    if action == 3:
        number_of_participants = int(input("Enter the number of participants: "))
        UI.print_top_number_students(list_of_students, number_of_participants)
    if action == 4:
        number_of_participants = int(input("Enter the numbers of participants: "))
        problem_index = int(input("Enter the problem number: "))
        UI.print_top_number_students(list_of_students, number_of_participants, problem_index)


def menu():
    list_of_students = functions.get_random_list_of_students()
    undo_list_of_student = []

    while True:
        print_menu()

        command = input("Enter your option:~")
        print("\n")

        commands = {1: add_and_insert_menu, 2: remove_and_replace_menu, 3: property_menu,
                    4: characteristic_menu}

        undo_commands = [1, 2]

        if command == 'x':
            break

        command = int(command)

        if command == 5:
            if undo_list_of_student:
                UND.undo(list_of_students, undo_list_of_student)
            else:
                print("There aren't any actions to be undone!")
                print("\n")
                time.sleep(2)
            continue

        if command in undo_commands:
            UND.save_current_state(list_of_students, undo_list_of_student)

        try:
            commands[int(command)](list_of_students)
        except KeyError:
            print("Invalid command\n")
            time.sleep(2)
        except TypeError:
            print("Invalid type for the arguments\n")
            time.sleep(2)
        except IndexError:
            print("ERROR: Problem scores must be in (0, 10) range\n")
            time.sleep(2)
        except ValueError:
            print("Invalid value for the arguments")
            time.sleep(2)
import time
import Modular_programming.domain as domain
import Modular_programming.contest_functions as functions
import Modular_programming.undo as UNDO
from Modular_programming.tests import *


def print_console_based_menu():
    print("Welcome to the menu! Chose an action :\n"
          "add <P1 score> <P2 score> <P3 score> // adds a new participant with scores p1,p2 and p3\n"
          "insert <P1 score> <P2 score> <P3 score> at <position> // insert scores p1,p2 and p3 at position in the list "
          "(*positions are indexed from 0)\n"              
          "remove <position> // set the scores of the participant at position <position> to 0\n"
          "remove <start position> to <end position> // set the scores of participants at positions 0,1,2...n to 0 "
          "(*positions are indexed from 0)\n"
          "remove [ < | = | > ] <score> // set the scores of participants having an average score <=> <score> to 0\n"    
          "replace <position> <P1 | P2 | P3> with <new score> // – replace the score obtained by participant position "
          "at Px with new_score\n"
          "list // write the list of participants and their scores for each problem\n"
          "list sorted // – write the participants sorted in decreasing order of their average score\n"
          "list [ < | = | > ] <score> // write the participants having an average score < = > than <score>\n"
          "avg <start_position> to <end_position> – writes the average of the average scores for participants between "
          "positions <start_position> and <end_position> in the list\n"
          "min <start_position> to <end_position> – writes the lowest average score for participants between "
          "positions <start_position> and <end_position> in the list\n"
          "top <number> // write the <number> participants having the highest average score,in descending order "
          "of their average score.\n"
          "top <number> <P1 | P2 | P3> // – write the <number> participants who obtained the highest score for "
          "problem <PX>, sorted descending by that score\n"
          "undo // the last operation will be reversed\n"

          "x exits the application")


def print_average_score_between_two_positions(list_of_students, start_position, end_position):
    average_score = functions.get_average_between_two_positions(list_of_students, start_position, end_position)
    print("The average of the average scores of the participants between positions {0} and {1} is: {2}\n".format(
        start_position, end_position, average_score
    ))
    time.sleep(4)


def print_minimum_average_score_between_two_positions(list_of_students, start_position, end_position):
    average_score = functions.get_minimum_average_between_two_positions(list_of_students, start_position, end_position)
    print("The minimum average score of the participants between positions {0} and {1} is: {2}\n".format(
        start_position, end_position, average_score
    ))
    time.sleep(4)


def print_top_number_students(list_of_students, number_of_students, problem_number=None):
    if problem_number is None:
        top_number_students = functions.get_top_number_students(list_of_students, number_of_students)
        number_of_students = int(number_of_students)

        for iterator in range(0, number_of_students):
            student = top_number_students[iterator]
            average = functions.get_average_score_for_student(student)
            position = functions.get_position_from_student(student)

            print("{0}!! : ".format(iterator+1), "Student #{0}: Avg: {1}; P1 = {2}; P2 = {3}; P3 = {4}".format(
                position, average, domain.get_problem1_score(student), domain.get_problem2_score(student),
                domain.get_problem3_score(student)))

        print("\n")
        time.sleep(4)
    else:
        if problem_number in "123":
            top_number_students = functions.get_top_number_students(list_of_students, number_of_students, problem_number)
            number_of_students = int(number_of_students)

            print("The best {0} students' score at problem {1} are: ".format(number_of_students, problem_number))
            for iterator in range(0, number_of_students):
                student = top_number_students[iterator]
                position = functions.get_position_top_from_student(student)

                print("{0}!! : ".format(iterator + 1), "Student #{0}: P1 = {1}; P2 = {2}; P3 = {3}".format(
                    position, domain.get_problem1_score(student), domain.get_problem2_score(student),
                    domain.get_problem3_score(student)))
        else:
            raise IndexError

        print("\n")
        time.sleep(4)


def print_students_in_list(list_of_students, string=None, average_score_needed=None):
    # ################################################## NORMAL LIST ##########################################
    if string is None:  # The simple "list" command
        print("These are the current students in the list: ")
        for iterator in range(0, len(list_of_students)):
            student = list_of_students[iterator]
            print("Student #{0}'s scores: P1 = {1};  P2 = {2}; P3 = {3};".format(
                iterator, domain.get_problem1_score(student), domain.get_problem2_score(student), domain.get_problem3_score(student)))
        time.sleep(5)
        print("\n\n")
    else:
        # ################################## SORTED LIST ################################################
        if string == "sorted":  # This gets called if command is "list sorted"
            list_of_sorted_students = functions.get_sorted_list_of_students(list_of_students)

            for student in list_of_sorted_students:
                average = functions.get_average_sorted_from_student(student)
                position = functions.get_position_from_student(student)

                print("Student #{0}: Avg: {1}; P1 = {2}; P2 = {3}; P3 = {4}".format(
                    position, average, domain.get_problem1_score(student), domain.get_problem2_score(student),
                    domain.get_problem3_score(student)))

            time.sleep(5)
            print("\n\n")

        # ########################################### LIST < VALUE ##############################################
        if ("<" in string) or (">" in string) or ("=" in string):  # This is called for "list <=> score"
            average_score_needed = int(average_score_needed)
            relation_sign = string

            for iterator in range(0, len(list_of_students)):
                if relation_sign == "<":
                    student = list_of_students[iterator]
                    average = functions.get_average_score_for_student(student)
                    if average < average_score_needed:
                        print("Student #{0}: Avg: {1}; P1 = {2}; P2 = {3}; P3 = {4}".format(
                            iterator, average, domain.get_problem1_score(student), domain.get_problem2_score(student),
                            domain.get_problem3_score(student)))

                if relation_sign == ">":
                    student = list_of_students[iterator]
                    average = functions.get_average_score_for_student(student)
                    if average > average_score_needed:
                        print("Student #{0}: Avg: {1}; P1 = {2}; P2 = {3}; P3 = {4}".format(
                            iterator, average, domain.get_problem1_score(student), domain.get_problem2_score(student),
                            domain.get_problem3_score(student)))

                if relation_sign == "=":
                    student = list_of_students[iterator]
                    average = functions.get_average_score_for_student(student)
                    if average == average_score_needed:
                        print("Student #{0}: Avg: {1}; P1 = {2}; P2 = {3}; P3 = {4}".format(
                            iterator, average, domain.get_problem1_score(student), domain.get_problem2_score(student),
                            domain.get_problem3_score(student)))

            time.sleep(5)
            print("\n")


def menu():
    list_of_students = functions.get_random_list_of_students()
    undo_list_of_student = []
    test_all_functions()

    while True:
        print_console_based_menu()

        command = input("Enter your command: ")

        commands = {"add": functions.add_student_to_list, "list": print_students_in_list,
                    "insert": functions.insert_student_with_score_to_a_position_in_list,
                    "remove": functions.remove_score_from_student,
                    "replace": functions.replace_score_in_position, "avg": print_average_score_between_two_positions,
                    "min": print_minimum_average_score_between_two_positions, "top": print_top_number_students}

        undo_commands = ["add", "insert", "remove", "replace"]

        if command == 'x':
            print("\n")
            print("You have closed the application!\n")
            break

        if command == "undo":
            if undo_list_of_student:
                UNDO.undo(list_of_students, undo_list_of_student)
            else:
                print("There aren't any actions to be undone!")
                print("\n")
                time.sleep(2)
            continue

        key_word, arguments = functions.compute_command_arguments(command)
        functions.compute_arguments(arguments) # We catch the keywords

        if key_word in undo_commands:
            UNDO.save_current_state(list_of_students, undo_list_of_student)

        # We get the key word(the command which will be executed) and the arguments for each command
        print("\n")  # Prints blank lines for visual effect

        try:
            commands[key_word](list_of_students, *arguments)
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











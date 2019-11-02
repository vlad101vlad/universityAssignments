import Modular_programming.domain as domain
import random
import Modular_programming.errors as ERROR


def get_random_list_of_students():
    """
    This function generates 10 random students into the list (as requested in the assignment rules)
    :return: A list of students
    """
    list_of_students = []
    for iterator in range(0, 10):
        score1, score2, score3 = random.randint(0, 10), random.randint(0, 10), random.randint(0, 10)
        list_of_students.append([score1, score2, score3])
    return list_of_students


def add_student_to_list(list_of_students, problem1_score, problem2_score, problem3_score):
    """
        This function adds a new participant to the list
    :param list_of_students: A list of students [probem1_score, problem2_score, problem3_score]
    :param probem1_score: String
    :param problem2_score: String
    :param problem3_score: String
    """
    probem1_score, problem2_score, problem3_score = int(problem1_score), int(problem2_score), int(problem3_score)

    if ERROR.problem_score_out_of_range(probem1_score, problem2_score, problem3_score):
        student = domain.create_student()
        domain.set_problem1_score(student, int(probem1_score))
        domain.set_problem2_score(student, int(problem2_score))
        domain.set_problem3_score(student, int(problem3_score))
        list_of_students.append(student)


def compute_command_arguments(command):
    """
    This function takes the command string and breaks it into key word and a list of arguments
    :param command:
    :return:
    """
    string_list = command.split()
    key_word = string_list[0]
    arguments = string_list[1:]
    return key_word, arguments


def insert_student_with_score_to_a_position_in_list(list_of_students, problem1_score, problem2_score, problem3_score, position):
    """
    This function inserts a new student to a give position into the list
    :param list_of_students: The list in which we will insert
    :param command_string: The raw string command inputted by the user
    :return: The new list_of_students
    """
    problem1_score, problem2_score, problem3_score = int(problem1_score), int(problem2_score), int(problem3_score)
    if ERROR.problem_score_out_of_range(problem1_score, problem2_score, problem3_score):
        list_of_students.append([0, 0, 0])  # We create a new entry for a the student to be inserted
        position = int(position)  # It is a string at first

        student = domain.create_student()
        domain.set_problem1_score(student, int(problem1_score))
        domain.set_problem2_score(student, int(problem2_score))
        domain.set_problem3_score(student, int(problem3_score))

        for iterator in range(len(list_of_students)-1, position, -1):
            list_of_students[iterator] = list_of_students[iterator-1]

        list_of_students[position] = student


def remove_score_from_student(list_of_students, start_position, end_position=None):
    """
    This function removes the score from a certain student (or from multiple students)
    :param list_of_students:
    :param start_position:
    :param end_position:
    :return:
    """
    if end_position is None:
        position = int(start_position)
        list_of_students[position] = domain.create_student()
    else:
        if start_position in "<=>":
            sign = start_position
            average_required = float(end_position)

            for iterator in range(len(list_of_students)):
                average = get_average_score_for_student(list_of_students[iterator])

                if sign == "=" and (average == average_required):
                    list_of_students[iterator] = domain.create_student()
                if sign == ">" and (average > average_required):
                    list_of_students[iterator] = domain.create_student()
                if sign == "<" and (average < average_required):
                    list_of_students[iterator] = domain.create_student()
        else:
            start_position = int(start_position)
            end_position = int(end_position)

            for iterator in range(start_position, end_position+1):
                list_of_students[iterator] = domain.create_student()


def replace_score_in_position(list_of_students, student_number, problem_index, new_score):
    """
    This function replace the score of participant at a certain problem
    :param list_of_students:
    :param student_number:
    :param problem_index:
    :param new_score:
    :return:
    """
    student_number = int(student_number)
    new_score = int(new_score)
    problem_index = int(problem_index)

    if new_score not in range(0, 11) or problem_index not in range(1, 4):
        raise IndexError
    else:
        if problem_index == 1:
            new_student = domain.create_student()
            domain.set_problem1_score(new_student, new_score)
            domain.set_problem2_score(new_student, domain.get_problem2_score(list_of_students[student_number]))
            domain.set_problem3_score(new_student, domain.get_problem3_score(list_of_students[student_number]))
            list_of_students[student_number] = new_student
            #domain.set_problem1_score(list_of_students[student_number], new_score)
        if problem_index == 2:
            new_student = domain.create_student()
            domain.set_problem1_score(new_student, domain.get_problem1_score(list_of_students[student_number]))
            domain.set_problem2_score(new_student, new_score)
            domain.set_problem3_score(new_student, domain.get_problem3_score(list_of_students[student_number]))
            list_of_students[student_number] = new_student
        if problem_index == 3:
            new_student = domain.create_student()
            domain.set_problem1_score(new_student, domain.get_problem1_score(list_of_students[student_number]))
            domain.set_problem2_score(new_student, domain.get_problem2_score(list_of_students[student_number]))
            domain.set_problem3_score(new_student, new_score)
            list_of_students[student_number] = new_student
            #domain.set_problem3_score(list_of_students[student_number], new_score)


def get_average_score_for_student(student):
    """
    This function gets the average score for a student
    :param student:
    :return:
    """
    problem1_score = domain.get_problem1_score(student)
    problem2_score = domain.get_problem2_score(student)
    problem3_score = domain.get_problem3_score(student)
    average = (problem1_score + problem2_score + problem3_score) / 3
    return average


def sort_by_first_element(value):
    return value[3]


def get_sorted_list_of_students(list_of_students):
    """
    This function sorts the list of participant into reversed order, the order being imposed by the average score
    to the problems
    :param list_of_students:
    :return:
    """
    student_with_average_list = []

    for iterator in range(0, len(list_of_students)):
        student_with_average = domain.create_student()
        student_with_average = list_of_students[iterator]
        average = get_average_score_for_student(student_with_average)

        student_with_average.append(average)  # We store the average for each student
        student_with_average.append(iterator)  # We store the position in the original list for each student

        student_with_average_list.append(student_with_average)

    student_with_average_list.sort(key=sort_by_first_element, reverse=True)
    return student_with_average_list


def get_average_between_two_positions(list_of_students, start_position, end_position):
    start_position, end_position = int(start_position), int(end_position)
    number_of_students = end_position - start_position + 1
    averages_sum = 0

    for iterator in range(start_position, end_position+1):
        averages_sum += get_average_score_for_student(list_of_students[iterator])

    return averages_sum / number_of_students


def get_minimum_average_between_two_positions(list_of_students, start_position, end_position):
    start_position, end_position = int(start_position), int(end_position)
    minimum_average = 11

    for iterator in range(start_position, end_position+1):
        student_average = get_average_score_for_student(list_of_students[iterator])
        if student_average < minimum_average:
            minimum_average = student_average
    return minimum_average


def sort_by_problem_x_score(student, problem_number):
    if problem_number == 1:
        return domain.get_problem1_score(student)
    if problem_number == 2:
        return domain.get_problem2_score(student)
    if problem_number == 3:
        return domain.get_problem3_score(student)


def get_top_number_students(list_of_students, number_of_students, problem_number=None):
    if problem_number is None:
        number_of_students = int(number_of_students)
        sorted_list_of_students = get_sorted_list_of_students(list_of_students)
        top_number_students = []

        for iterator in range(0, number_of_students):
            top_number_students.append(sorted_list_of_students[iterator])
        return top_number_students
    else:
        number_of_students = int(number_of_students)
        top_number_students = []

        for iterator in range(len(list_of_students)):
            list_of_students[iterator].append(iterator)

        list_of_students.sort(key=sort_by_problem_x_score(list_of_students, problem_number), reverse=True)

        for iterator in range(0, number_of_students):
            top_number_students.append(list_of_students[iterator])

        return top_number_students


def get_position_top_from_student(student):
    return student[3]


def get_position_from_student(student):
    return student[4]

def get_average_sorted_from_student(student):
    return student[3]

def compute_arguments(list_of_arguments):
    index = 0
    key_words = ["at", "to", "with"]

    while index < len(list_of_arguments):
        argument = list_of_arguments[index]
        if argument == "P1":
            list_of_arguments[index] = "1"
        if argument == "P2":
            list_of_arguments[index] = "2"
        if argument == "P3":
            list_of_arguments[index] = "3"

        if argument in key_words:
            for iterator in range(index, len(list_of_arguments)-1):
                list_of_arguments[iterator] = list_of_arguments[iterator+1]
            list_of_arguments.pop()
            index -= 1

        index += 1





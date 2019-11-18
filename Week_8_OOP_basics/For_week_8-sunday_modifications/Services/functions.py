import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Domain.entities as entity

def add_new_student_to_list(list_of_students, student_ID, student_name, student_group):
    new_student = entity.Student(student_ID, student_name, student_group)

    list_of_students.append(new_student)

def add_assignment_to_list(list_of_assignments, assignment_ID, description, deadline):
    new_assignment = entity.Assignment(assignment_ID, description, deadline)

    list_of_assignments.append(new_assignment)

def update_students_with_id(list_of_students,student_ID, new_name, new_group):
    stundent = find_student_by_ID(list_of_students, student_ID)
    stundent.set_name(new_name)
    stundent.set_group(new_group)

def update_assignments_with_id(list_of_assignments, assignment_ID, new_description, new_deadline):
    assignment = find_assignment_by_ID(list_of_assignments, assignment_ID)
    assignment.set_description(new_description)
    assignment.set_deadline(new_deadline)

def remove_student_from_list(list_of_students, student_ID):
    
    for iterator in range(len(list_of_students)):
        student = list_of_students[iterator]

        if student.student_ID == student_ID:
            for alternative_iterator in range(iterator, len(list_of_students) - 1):
                list_of_students[alternative_iterator] = list_of_students[alternative_iterator+1]
            list_of_students.pop()
            
            break

def get_all_the_groups_from_students(list_of_students):
    list_of_groups = []

    for student in list_of_students:
        if student.group not in list_of_groups:
            list_of_groups.append(student.group)

    return list_of_groups

def remove_assignment_from_list(list_of_assignments, assignment_ID):
    
    for iterator in range(len(list_of_assignments)):
        assignment = list_of_assignments[iterator]

        if assignment.assignment_ID == assignment_ID:
            for alternative_iterator in range(iterator, len(list_of_assignments) - 1):
                list_of_assignments[alternative_iterator] = list_of_assignments[alternative_iterator+1]
            list_of_assignments.pop()
            
            break



def format_list_of_students_in_print_form(list_of_students):
    print_form_list = []

    for iterator in range(len(list_of_students)):
        student = list_of_students[iterator]
        print_form_list.append(student.print_form)

    return print_form_list


def format_list_of_assignments_in_print_form(list_of_assignments):
    print_form_list = []

    for iterator in range(len(list_of_assignments)):
        assignment = list_of_assignments[iterator]
        print_form_list.append(assignment.print_form)

    return print_form_list


def find_students_in_a_given_group(list_of_students, group):
    list_of_students_in_group = []

    for iterator in range(len(list_of_students)):
        student = list_of_students[iterator]

        if student.group == group:
            list_of_students_in_group.append(student)

    return list_of_students_in_group


def find_student_by_ID(list_of_students, student_ID):
    """
        This function searches for a given student in the given list
        Returns :
        -> Student object if there is an ID corresponding to it
        -> Index Error if there isn't any student with the given ID
    """
    
    for student in list_of_students:
        if student.student_ID == student_ID:
            return student
            
    return IndexError

def find_assignment_by_ID(list_of_assignments, assignment_ID):
    """
    This function searches for a given assigment in the given list
    Returns :
    -> Assignment object if there is an ID corresponding to it
    -> Index Error if there isn't any student with the given ID
    """
    found = 0
    for assignment in list_of_assignments:
        if assignment.assignment_ID == assignment_ID:
            found = 1
            return assignment
            
    raise IndexError


def give_an_assigment_to_entity(list_of_students, assignment_object, item_from_entities):

    if type(item_from_entities) == entity.Student:
        
        if assignment_object.assignment_ID not in item_from_entities.assignment_list:
            item_from_entities.assignment_list.append(assignment_object.assignment_ID)
    
    else:
        try:
            group = int(item_from_entities)
            student_in_given_group = find_students_in_a_given_group(list_of_students, group)

            for student in student_in_given_group:
                if assignment_object.assignment_ID not in student.assignment_list:
                    student.assignment_list.append(assignment_object.assignment_ID)          

        except ValueError:
            print("The group number is an int")


# def update_after_assigment_removal(list_of_students, assignment_ID):
#     for student in list_of_students:
#         if assignment_ID in student.assignment_list:
#             student.assignment_list.remove(assignment_ID)

def update(list_of_students, list_of_assignments):
    
    # We store all the assigment ID's in a list
    assignment_ID_list = []
    for assignment in list_of_assignments:
        assignment_ID_list.append(assignment.assignment_ID)
    
    # We loop for each student through its assignment list to search if they have the removed assigment
    for student in list_of_students:
        for assignment in student.assignment_list:
            if assignment not in assignment_ID_list:    # We check if the current assignment in list is indeed a valid assignment
                student.assignment_list.remove(assignment)
    
        


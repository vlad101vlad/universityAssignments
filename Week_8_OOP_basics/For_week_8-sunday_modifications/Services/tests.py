import unittest
import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import Services.functions as functions
from Domain import entities as entities

class TestFunctions(unittest.TestCase):
    def test_add_new_student_to_list_ValidInput_ValueAdded(self):
        list_of_students = []
        functions.add_new_student_to_list(list_of_students, 1, "vlad-rares", 816)
        student = entities.Student(1, "vlad-rares", 816)

        self.assertListEqual(list_of_students, [student])

    
    def test_add_new_assignment_to_list_ValidInput_ValueAdded(self):
        list_of_assignments = []
        functions.add_assignment_to_list(list_of_assignments, 1, "make some egges", "2223232")
        assignment = entities.Assignment(1, "make some egges", "2223232")

        self.assertListEqual(list_of_assignments, [assignment])

    def test_remove_student_from_list_ValidInput_ValueRemoved(self):
        student = entities.Student(1, "vlad-rares", 816)
        list_of_students = [student]

        functions.remove_student_from_list(list_of_students, student.student_ID)

        self.assertListEqual(list_of_students, [])

    def test_get_all_the_groups_from_students_ValidInput_listOfGroupsReceived(self):
        student = entities.Student(1, "vlad-rares", 816)
        student2 = entities.Student(2, "bran", 212)
        student3 = entities.Student(3, "iohanis", 816)

        list_of_students = [student, student2, student3]
        list_of_groups = functions.get_all_the_groups_from_students(list_of_students)

        self.assertListEqual(list_of_groups, [816, 212])

    def test_remove_assignment_from_list(self):
        assignment = entities.Assignment(1, "do something", "08062019")
        assignment2 = entities.Assignment(19, "do something else", "21062019")

        list_of_assignments = [assignment, assignment2]
        functions.remove_assignment_from_list(list_of_assignments, 1)

        self.assertListEqual(list_of_assignments, [assignment2])
        
    def test_find_assignment_by_ID(self):
        assignment = entities.Assignment(1, "do something", "08062019")
        assignment2 = entities.Assignment(19, "do something else", "21062019")

        list_of_assignments = [assignment, assignment2]
        

        self.assertEqual(functions.find_assignment_by_ID(list_of_assignments, 19), assignment2)
        
        with pytest.raises(IndexError):
            assert functions.find_assignment_by_ID(list_of_assignments, 52)

    def test_find_students_in_a_given_group(self):
        student = entities.Student(1, "vlad-rares", 816)
        student2 = entities.Student(2, "bran", 212)
        student3 = entities.Student(3, "iohanis", 816)

        list_of_students = [student, student2, student3]
        self.assertListEqual(functions.find_students_in_a_given_group(list_of_students, 816), [student, student3] )


    def test_update(self):
        assignment = entities.Assignment(1, "do something", "08062019")
        assignment2 = entities.Assignment(19, "do something else", "21062019")

        student = entities.Student(1, "vlad-rares", 816)
        student2 = entities.Student(2, "bran", 212)
        student3 = entities.Student(3, "iohanis", 816)

        list_of_students = [student, student2, student3]
        list_of_assignments = [assignment, assignment2]

        functions.give_an_assigment_to_entity(list_of_students, assignment, student)
        functions.remove_assignment_from_list(list_of_assignments, 1)

        functions.update(list_of_students, list_of_assignments)

        self.assertListEqual(student.assignment_list, [])

    # def are_students_objects_equal(self, first_student, second_student):
    #     self.assertEqual( type(first_student), type(second_student) )
    #     self.assertEqual( first_student.student_ID, second_student.student_ID )
    #     self.assertEqual( first_student.name, second_student.name )
    #     self.assertEqual( first_student.group, second_student.group )

if __name__ == "__main__":
    unittest.main()

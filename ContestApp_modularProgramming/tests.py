from Modular_programming.contest_functions import *
from Modular_programming.domain import *
from Modular_programming.errors import *


def test_get_average_score_for_student_123_2():
    student = [1, 2, 3]
    assert(get_average_score_for_student(student) == 2)


def test_get_p1_score_529_5():
    student = [5, 2, 9]
    assert(get_problem1_score(student) == 5)


def test_problem_score_out_of_range_234_1():
    p1_score = 2
    p2_score = 3
    p3_score = 4
    assert( problem_score_out_of_range(p1_score, p2_score, p3_score) == 1)


def test_set_p1_score_423_10_1023():
    student = [4, 2, 3]
    set_problem1_score(student, 10)
    assert (student == [10, 2, 3])


def test_add_student_to_list_emptyList_studentWithScores234_listIs234():
    list = []
    add_student_to_list(list, 2, 3, 4)
    assert (list == [[2, 3, 4]])


def test_remove_score_from_student_234_000():
    list = [[2, 3, 4]]
    remove_score_from_student(list, 0)
    assert (list == [[0, 0, 0]])


def test_compute_arguments_start_with_car_returns_car():
    arguments = ["car", "with"]
    compute_arguments(arguments)
    assert (arguments == ["car"])


def test_compute_arguments_start_with_car_P2_return_car_2():
    arguments = ["car", "with", "P2"]
    compute_arguments(arguments)
    assert (arguments == ["car", '2'])


def test_all_functions():
    test_get_average_score_for_student_123_2()
    test_get_p1_score_529_5()
    test_problem_score_out_of_range_234_1()
    test_set_p1_score_423_10_1023()
    test_add_student_to_list_emptyList_studentWithScores234_listIs234()
    test_remove_score_from_student_234_000()
    test_compute_arguments_start_with_car_returns_car()
    test_compute_arguments_start_with_car_P2_return_car_2()
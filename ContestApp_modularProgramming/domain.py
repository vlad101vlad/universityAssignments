def create_student():
    return [0, 0, 0]


def get_problem1_score(student):
    return int(student[0])


def get_problem2_score(student):
    return int(student[1])


def get_problem3_score(student):
    return int(student[2])


def set_problem1_score(student, problem1_score):
    student[0] = problem1_score
    return student


def set_problem2_score(student, problem2_score):
    student[1] = problem2_score
    return student


def set_problem3_score(student, problem3_score):
    student[2] = problem3_score
    return student


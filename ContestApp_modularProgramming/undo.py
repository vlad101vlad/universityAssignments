def save_current_state(list_of_students, backup_list):
    backup_list.append(list_of_students[:])


def undo(list_of_students, backup_list):
    previous_student_list = backup_list.pop()
    list_of_students[:] = previous_student_list


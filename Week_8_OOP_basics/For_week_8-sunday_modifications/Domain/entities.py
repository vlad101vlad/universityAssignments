class Student:
    def __init__(self, student_ID, name, group):
        self._student_ID = student_ID
        self._name = name
        self._group = group
        self._assignment_list = [] # This list will store all the assigments given for a student, be it grade or ungraded    

    def __eq__(self, other):
        return self.student_ID == other.student_ID and self.name == other.name and self.group == other.group      

    @property
    def student_ID(self):
        return self._student_ID

    @property
    def name(self):
        return self._name
    
    def set_name(self, new_name):
        self._name = new_name

    def set_group(self, new_group):
        self._group = new_group

    @property
    def group(self):
        return self._group

    @property
    def assignment_list(self):
        return self._assignment_list

    @property
    def print_form(self):
        string_to_be_printed = "Student #{id}: ".format(id=self.student_ID)
        string_to_be_printed = string_to_be_printed + "[{name}] is in group [{group}]".format(name = self.name, group = self.group)
        string_to_be_printed = string_to_be_printed + " and has assigments: {list}".format(list = self.assignment_list)
        return string_to_be_printed


class Assignment:
    def __init__(self, assignment_ID, description, deadline):
        self._assignment_ID = assignment_ID
        self._description = description
        self._deadline = deadline

    def __eq__(self, other):
        return self.assignment_ID == other.assignment_ID and self.description == other.description and self.deadline == other.deadline

    @property
    def assignment_ID(self):
        return self._assignment_ID

    @property
    def description(self):
        return self._description

    @property
    def deadline(self):
        return self._deadline

    def set_description(self, new_description):
        self._description = new_description

    def set_deadline(self, new_deadline):
        self._deadline = new_deadline

    @property
    def print_form(self):
        string_to_be_printed = "Assignment #{id}: ".format(id=self.assignment_ID)
        string_to_be_printed = string_to_be_printed + "{description} /// Deadline: {deadline}".format(description = self.description, deadline = self.deadline)
        return string_to_be_printed


class Grade:
    def __init__(self, Assignment, Student, grade):
        self._assignment_ID = Assignment.assignment_ID
        self._student_ID = Student.student_ID
        self.grade = grade

    @property
    def assignment_ID(self):
        return self._assignment_ID

    @property
    def student_ID(self):
        return self._student_ID

    @property
    def grade(self):
        return self.grade
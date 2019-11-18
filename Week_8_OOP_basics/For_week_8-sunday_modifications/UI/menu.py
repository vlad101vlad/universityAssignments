import Services.functions as functions


def print_menu():
    print("\n       Welcome to the menu! Choose and action: \n\n",
        "1: Add a new student to the list\n",
        "2: Print the students in the list\n",
        "3: Add a new assignment to the list\n",
        "4: Print the assignments in the list \n",
        "5: Remove a student from the list\n",
        "6: Remove assignment from the list\n",
        "7: Give an assignment\n",
        "8: Update a student\n",
        "9: Update an assignment\n",
        "x ~ Exits the application \n"
    )

def add_10_students_to_the_list(list_of_students):
    functions.add_new_student_to_list(list_of_students, 0, "Raducu Vlad-Rares", 916)
    functions.add_new_student_to_list(list_of_students, 1, "Jurj Mihai", 215)
    functions.add_new_student_to_list(list_of_students, 2, "Banciu Raul", 215)
    functions.add_new_student_to_list(list_of_students, 3, "Pasca Eduard-Marian", 916)
    functions.add_new_student_to_list(list_of_students, 4, "Balacescu Vlad-Ionut", 916)
    functions.add_new_student_to_list(list_of_students, 5, "Stoicescu Sebastian", 217)
    functions.add_new_student_to_list(list_of_students, 6, "Popescu Andrei", 711)
    functions.add_new_student_to_list(list_of_students, 7, "Clesiu Vlad", 217)
    functions.add_new_student_to_list(list_of_students, 8, "Magdau Alexandru", 422)
    functions.add_new_student_to_list(list_of_students, 9, "Mezei Bodan", 422)

def add_3_assignments_to_the_list(list_of_assignments):
    functions.add_assignment_to_list(list_of_assignments, 0, "Construct a file", "22102019")
    functions.add_assignment_to_list(list_of_assignments, 1, "Do 5 exercices from page 18", "21112019")
    functions.add_assignment_to_list(list_of_assignments, 2, "Make a reasearch paper on tests", "01022020")
    functions.add_assignment_to_list(list_of_assignments, 3, "Learn Pytagora's theorem", "21112019")
    functions.add_assignment_to_list(list_of_assignments, 4, "Solve the exercices from the seminar", "19112019")
    functions.add_assignment_to_list(list_of_assignments, 5, "Study for the mid-term exam", "07122019")
    functions.add_assignment_to_list(list_of_assignments, 6, "Clean the bathroom", "18112019")
    functions.add_assignment_to_list(list_of_assignments, 7, "Make a reasearch paper on elephants", "01022020")
    functions.add_assignment_to_list(list_of_assignments, 8, "Make a reasearch paper on monkeys", "01022020")
    functions.add_assignment_to_list(list_of_assignments, 9, "Make a reasearch paper on donkeys", "01022020")


def add_new_student(list_of_students):
    try:
        student_ID = list_of_students[-1].student_ID + 1 
        name = input("      Enter the student's name:~ ")
        group = int(input("    Enter the student's group:~ "))

        functions.add_new_student_to_list(list_of_students, student_ID, name, group)
    except ValueError:
        print("The group number has to be of type:int")


def add_new_assignment(list_of_assignments): 
    assignment_ID = list_of_assignments[-1].assignment_ID + 1
    description = input("      Enter the assignment's description:~ ")
    deadline = input("    Enter the assignment's deadline:~ ")

    functions.add_assignment_to_list(list_of_assignments, assignment_ID, description, deadline)
    
def update_a_student(list_of_students):
    try:
        print("Choose the student you wish to update: ")
        print_list_of_students(list_of_students)

        student_ID = int(input("ID~ "))
        new_name = input("New name: ")
        new_group = int(input("New group: "))

        functions.update_students_with_id(list_of_students, student_ID, new_name, new_group)
    
    except ValueError:
        print("Student ID/Group must be int")
    except IndexError:
        print("There isn't a student with such ID")

def update_an_assignment(list_of_assignments):
    try:
        print("Choose the assignements you wish to update: ")
        print_list_of_assignments(list_of_assignments)

        assignment_ID = int(input("ID~ "))
        new_description = input("New description: ")
        new_deadline = input("New deadline: ")

        functions.update_assignments_with_id(list_of_assignments, assignment_ID, new_description, new_deadline)
    
    except ValueError:
        print("Student ID/Group must be int")
    except IndexError:
        print("There isn't a student with such ID")

def print_list_of_students(list_of_students):
    print_form_list = functions.format_list_of_students_in_print_form(list_of_students)

    for student in print_form_list:
        print(student)
    print("\n")


def remove_student(list_of_students):
    print_list_of_students(list_of_students)
    print("Which student you wish to remove? Enter their ID:")

    try:
        command = int(input("Enter student's ID:~ "))
        student = list_of_students[command]

        print("\nYou wish to remove the student #{id} : {name}".format(id = student.student_ID, name = student.name ))
        choice = input("Press:\n 1 -> Remove the student\n x -> Any other key to return to menu: \n Input:~")

        if choice == "1":
            functions.remove_student_from_list(list_of_students, student.student_ID )
            print("You have removed a student from the list!\n\n")
        else:
            return
    except ValueError:
        print("Invalid value for the command (must be type:int)")


def remove_assignment(list_of_assignments):
    print_list_of_assignments(list_of_assignments)
    print("Which assignment do you wish to remove? Enter its ID:")

    try:
        command = int(input("Enter assignment's ID:~ "))
        assignment = list_of_assignments[command]

        print("\nYou wish to remove the assignment #{id} : {description}".format(id = assignment.assignment_ID, description = assignment.description ))
        choice = input("Press:\n 1 -> Remove the assignment\n x -> Any other key to return to menu: \n Input:~")

        if choice == "1":
            functions.remove_assignment_from_list(list_of_assignments, assignment.assignment_ID )
            print("You have removed a student from the list!\n\n")
        else:
            return
    except ValueError:
        print("Invalid value for the command (must be type:int)")
    except IndexError:
        print("There aren't assignemnts for the inputed ID")


def print_list_of_assignments(list_of_assignments):
    print_form_list = functions.format_list_of_assignments_in_print_form(list_of_assignments)

    for assignment in print_form_list:
        print(assignment)
    print("\n")

def give_an_assigment(list_of_students, list_of_assignments):
    print("Please enter the assignment ID:")
    print_list_of_assignments(list_of_assignments)
    
    try:
        assigment_ID = int(input("Input:~ "))
        assignment = functions.find_assignment_by_ID(list_of_assignments, assigment_ID)


        print("You can give an assigment either to a student or a group of students. Press:\n",
            "1: Give an assigment to a student\n",
            "2: Give an assigment to a group of students\n"
        )
        try:
            choice = int(input("Input:~ "))

            if choice == 1:
                print_list_of_students(list_of_students)
                student_id = int(input("Student ID:~ "))

                student = functions.find_student_by_ID(list_of_students, student_id)
                functions.give_an_assigment_to_entity(list_of_students, assignment, student)
                          

            if choice == 2:
                print("Available groups:")
                print(functions.get_all_the_groups_from_students(list_of_students))
                
                group = int(input("Group:~ "))
                if group in functions.get_all_the_groups_from_students(list_of_students):
                    functions.give_an_assigment_to_entity(list_of_students, assignment, group)
                else:
                    raise IndexError

        except ValueError:
            print("Choice must be type:int")
        except IndexError:
            print("There is no student/group with such ID")
            
    except ValueError:
        print ("Assigment ID must be type:int")



def main_menu():
    list_of_students = []
    add_10_students_to_the_list(list_of_students)

    list_of_assignments = []
    add_3_assignments_to_the_list(list_of_assignments)


    while True:
        print_menu()
       
        command = input("Enter your command:~ ")

        if command == 'x':
            print("You have closed the application\n")
            break
            
        commands = {
            1:add_new_student, 
            2:print_list_of_students,
            3:add_new_assignment,
            4:print_list_of_assignments,
            5:remove_student,
            6:remove_assignment,
            7:give_an_assigment,
            8:update_a_student,
            9:update_an_assignment}
        
        destructive_commands = [5, 6]

        try:
            command = int(command)

            if command in [1, 2, 5, 8]: # Commands with list of students as argument
                commands[command](list_of_students)
            
            if command in [3, 4, 6, 9]: # Commands which need list of assignments as argument
                commands[command](list_of_assignments)

            if command in [7]: # Commands which need both list as arguments
                commands[command](list_of_students, list_of_assignments) 

            if command in destructive_commands:
                functions.update(list_of_students, list_of_assignments)

        except ValueError:
            print("Invalid type for the command")
        except KeyError:
            print("We have not implemented a feature for this key")


def print_operation_matrix(operation_matrix, n_elements):

    print_operation_matrix.counter += 1


    print('\n'.join([''.join(['{:4}'.format(item+1) for item in row])
                     for row in operation_matrix]))



print_operation_matrix.counter = 0

def check_if_associative(operation_matrix, n_elements):
    # Rule if (a * b) * c =  a * (b*c)

    for i in range(0, n_elements):
        for j in range(0, n_elements):
            for k in range(0, n_elements):
                if operation_matrix[operation_matrix[i][j]][k] != operation_matrix[i][operation_matrix[j][k]]:
                    return 0

    return 1



def generate_operation_matrix(operation_table, n_elements):
    operation_matrix = []

    counter = 0
    for i in range(0, n_elements):
        operation_matrix.append([])
        for j in range(0, n_elements):
            operation_matrix[i].append(operation_table[counter])
            counter += 1

    return operation_matrix



def get_all_operations(n_elements, index, operation):
    if index > n_elements * n_elements:
        operation_matrix = generate_operation_matrix(operation, n_elements)
        if(check_if_associative(operation_matrix, n_elements)):
            print_operation_matrix(operation_matrix, n_elements)
            print("\n")
    else:
        for i in range(0, n_elements):
            operation.append(i)
            get_all_operations(n_elements, index+1, operation)
            operation.pop()
        return


if __name__ == '__main__':
    set = []
    n = int(input("Enter the number of elements of the set A: "))

    for i in range(0, n):
        set.append(i+1)

    operation = []
    print("The matrices coresponding to the operations tables for the set A = {0} are:".format(set))
    get_all_operations(n, 1, operation)
    print("The number of associative operations on a set A = {0} is {1}".format(set, print_operation_matrix.counter))
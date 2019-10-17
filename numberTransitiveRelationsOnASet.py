def populate_set(set):
    """
    This function receives a set as an argument and it populates it whith n elements, from 1 to n
    n is input from the user

    """
    n = int(input("Enter number of elements: "))
    for i in range(1, n+1):
        set.append(i)

def print_set(set):
    """
    This function prints a given set
    """
    print_set.counter += 1
    print("R{0}: ".format(print_set.counter), end="")
    print(set)

print_set.counter = 0

def make_pair_set(set):
    """
        This function returns all the possible relations between the elements of a set
    """
    pairs_set = []
    for i in range(0, len(set)):
        for j in range(0, len(set)):
            pairs_set.append([set[i], set[j]])
    return pairs_set

def generate_subSet(big_set, subset, index, n_elements):
    """
            This is a "backtracking" function which works as follows:
            It receives a big_set for which it generates all the sub_sets of that particular big_set
            In order to see which are transitive relations for a set , we need to generate all the sub_sets and check if
        they are transitive of not
    """
    relation_list = get_realtion_list(subset, n_elements) # We get the relation list for a subset


    if check_if_transitive(relation_list, subset, n_elements) == 1: #We check if it is transitive
        print_set(subset)   #If it is, we print it to the screen

    for i in range(index, len(big_set)):    #The recursive part of the function, it generates all the possible subsets
        subset.append(big_set[i])
        generate_subSet(big_set, subset, i+1, n_elements)
        subset.pop(-1)
    return

def get_subSets(set, n_elements): # Generates the subsets for a given set
    subSet = []
    index = 0
    generate_subSet(set, subSet, index, n_elements)

def check_if_transitive(relation_list, set, n_elements):
    """
        This function checks if a function is transitive or not
        Given a relation list, it loop through every element
        In order to be transitive, we have to respect the following codition:
            relation_list[i][j] == 1 -> It exists a relation from i to j
            Now we have to loop through all the relations which start from j
            relation_list[j][k] -> If this is true, that means we also have
            relation_list[i][k] (in order to be transitive)
            If it is false , we exit the function and the subset is not transitive

            The functions stops when it checked all the possible relations
    """
    for i in range(0, n_elements):
        for j in range(0, n_elements):
            if relation_list[i][j] == 1:
                for k in range(0, n_elements):
                    if relation_list[j][k] == 1 and relation_list[i][k] == 0:
                        return 0

    return 1

def get_realtion_list(subSet, n_elements):
    """
        This function generates the relation matrix for a given set relation
        It has the property:
            if (a,b) exists relation_list[a][b] = 1
            else relation_list[a][b] = 0
    """
    relation_list = [ [0 for i in range(0, n_elements)] for i in range(0, n_elements) ] # This creates a matrix which is
    # initialised on 0.

    for i in range(0, len(subSet)):
        x = subSet[i][0]
        y = subSet[i][1]
        relation_list[x-1][y-1] = 1
    return relation_list


if __name__ == '__main__':


    set = [] #We create the set of n element
    pairs_set = [] #We create the relation set
    populate_set(set) #We populate the set of n elements
    pairs_set = make_pair_set(set) #We populate the relation set


    print("The transitive relations on a set A = {0} are: ".format(set))
    get_subSets(pairs_set, len(set)) # We apply the algorithm
    print("The number of transitive relations on a set A = {0} is {1}".format(set, print_set.counter))




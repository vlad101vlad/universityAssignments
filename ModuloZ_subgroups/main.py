
def generate_pair_set(m, n):
    """
    This function generates all the possible pairs with the property (a,b) / a in Zm and b in Zn
    :return: The set of all possible pairs
    """
    pairs_set = []
    for i in range (0, m):
        for j in range(0, n):
            pair = [i, j]
            pairs_set.append(pair)

    return pairs_set


def generate_sub_sets(big_set, index, subset, m, n):
    """
    This function uses a backtracking algorithm in order to generate all the possible subsets of the pairs_set
    After we found a subset , we check whether it is a stable part and print it if it is
    """

    if check_if_stable(subset, m, n) and len(subset) != 0:
        print_subset(subset, big_set, m, n)

    if index > len(big_set)-1:
        ok = 1
    else:
        for i in range(index, len(big_set)):
            subset.append(big_set[i])
            generate_sub_sets(big_set, i+1, subset, m, n)
            subset.pop()
        return


def check_if_stable(subset, m, n):
    """
    This function checks whether a given subset is a stable part
    :param subset:
    :param m:
    :param n:
    :return:
    """
    new_pair = []
    for i in range(0, len(subset)):
        for j in range(0, len(subset)):
            pair1 = subset[i]
            pair2 = subset[j]
            new_pair.append( (pair1[0] + pair2[0]) % m )
            new_pair.append( (pair1[1] + pair2[1]) % n )
            if subset.count(new_pair) == 0:
                return 0
            new_pair = []

    return 1

def print_subset(subset, big_set, m, n):
    print_subset.counter += 1

    if subset == big_set:
        print("H{0} =  Z{1} x Z{2}".format(print_subset.counter, m, n))
    else:
        print("H{0} =  {1} ".format(print_subset.counter, subset))

print_subset.counter = 0

if __name__ == '__main__':
    print("Input:")
    m = int(input("m := "))
    n = int(input("n := "))
    print("*****************\n")

    print("The subgroups of the abelian group (Z{0} × Z{1}, +) are: \n".format(m, n))
    pairs_set = []
    pairs_set = generate_pair_set(m, n)
    subset = []

    generate_sub_sets(pairs_set, 0, subset, m, n)
    print("The number of subgroups of the abelian group (Z{0} × Z{1}, +) is : {2}".format(m, n, print_subset.counter))


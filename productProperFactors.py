'''
[9]Consider a given natural number n. Determine the product p of all the proper factors of n.
'''

def product_proper_factors(number):
    '''The function computes the product of the proper factors of n
    
    :param n: Natural number for which we compute the product of its proper factors
    :return: The product of the proper factors of n.
    '''
    product = 1
    for iterator in range(2, number//2+1):
        if number % iterator == 0:
            product *= iterator

    if product == 1:
        return 0
    return product

if __name__ == '__main__':
    number = int(input("n = "))
    print("The product of all the proper factors of {0} is: {1} ".format(number, product_proper_factors(number)))
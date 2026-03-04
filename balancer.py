from random import randint
from math import gcd
from functools import reduce


def balance(moleculeParser):

    balanced = False

    while not balanced:

        reactants, products = moleculeParser

        temp_left = [dict(i) for i in reactants]
        temp_right = [dict(i) for i in products]

        total_left = {}
        total_right = {}

        left_coefficients = [randint(1,10) for _ in temp_left]
        right_coefficients = [randint(1,10) for _ in temp_right]

        # multiply reactants
        for i in range(len(temp_left)):
            for element in temp_left[i]:
                temp_left[i][element] *= left_coefficients[i]
                total_left[element] = total_left.get(element,0) + temp_left[i][element]

        # multiply products
        for i in range(len(temp_right)):
            for element in temp_right[i]:
                temp_right[i][element] *= right_coefficients[i]
                total_right[element] = total_right.get(element,0) + temp_right[i][element]

        # compare elements
        balanced = total_left == total_right


    big_tup = tuple(left_coefficients + right_coefficients)
    g = reduce(gcd, big_tup)

    left_coefficients = [int(x/g) for x in left_coefficients]
    right_coefficients = [int(x/g) for x in right_coefficients]


    string = ""

    # left side
    for i,compound in enumerate(reactants):

        coeff = "" if left_coefficients[i] == 1 else str(left_coefficients[i])

        comp = coeff
        for e in compound:
            comp += e
            if compound[e] != 1:
                comp += str(compound[e])

        string += comp + " + "

    string = string[:-3] + " = "

    # right side
    for i,compound in enumerate(products):

        coeff = "" if right_coefficients[i] == 1 else str(right_coefficients[i])

        comp = coeff
        for e in compound:
            comp += e
            if compound[e] != 1:
                comp += str(compound[e])

        string += comp + " + "

    string = string[:-3]

    return string


if __name__ == '__main__':
    print(balance(([{'C': 1, 'O': 2}, {'H': 2, 'O': 1}], [{'C': 6, 'H': 12, 'O': 6}, {'O': 2}])))

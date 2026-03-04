# technique 1
# import string
# # Remove all whitespaces
# chemical_input_taker = input("Enter the chemical equation: ")
# translation_table = str.maketrans('', '', string.whitespace)
# no_spaces_chemical_input_taker = chemical_input_taker.translate(translation_table)

# # seperate reactants and products
# reactants_and_products = no_spaces_chemical_input_taker.split('->')
# print(reactants_and_products)

# # seperate reactants
# reactants = reactants_and_products[0].split('+')
# print(reactants)

# # seperate products
# products = reactants_and_products[1].split('+')
# print(products)


# architecture 2
def eq_seperator(reactants, products):
    reactants_list = reactants.split("+")
    products_list = products.split("+")
    
    return reactants_list, products_list


if __name__ == '__main__':
    print(eq_seperator('CO2+H2O', 'C6H12O6+O2'))
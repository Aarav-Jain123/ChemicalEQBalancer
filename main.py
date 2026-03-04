from eqSeperator import eq_seperator
from moleculeParser import molecule_parser
from balancer import balance
from balancerSympy import balance_sympy

print('Insert chemical equation with elements in\nparentheses followed by the number of atoms:')
print('''Example: 
For reactants: HCl+KOH
For products: KCl+H2O''')
reactants = input(">>> ")
products = input(">>> ")


step1 = eq_seperator(reactants, products)
step2 = molecule_parser(step1)
step3 = balance(step2)
print(step3)

# if u want to, you can use the balancer2 which was made usign sympy, just replace the balance in line 16 to balance_sympy
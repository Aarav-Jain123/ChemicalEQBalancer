def molecule_parser(eq_seperator):
    def parse_molecule(molecule):
        # the stack handles nested parentheses. 
        # stack[0] is our main container for the whole molecule.
        stack = [{}]
        i = 0
        
        while i < len(molecule):
            # handles the start of a group: (
            if molecule[i] == '(':
                stack.append({})  # pushes a new empty dictionary in to the stack
                i += 1
                
            # 2. handles the end of the group:
            elif molecule[i] == ')':
                i += 1
                # checks for a multiplier after the bracket
                num = ''
                while i < len(molecule) and molecule[i].isdigit():
                    num += molecule[i]
                    i += 1
                
                multiplier = int(num) if num else 1
                group = stack.pop()  # removes the recent dictionary
                
                # multiply everything in that dictioanry and then adds it to the level below
                for element, count in group.items():
                    stack[-1][element] = stack[-1].get(element, 0) + count * multiplier
            
            # 3. handles the element symbols
            elif molecule[i].isupper():
                element = molecule[i]
                i += 1
                # if the next letter is lowercase, it belongs to this element
                if i < len(molecule) and molecule[i].islower():
                    element += molecule[i]
                    i += 1
                
                # looks for the number of atoms
                num= ''
                while i < len(molecule) and molecule[i].isdigit():
                    num += molecule[i]
                    i += 1
                
                # if no number is found, then it automatically assigns 1 atom
                count = int(num) if num else 1
                # adds this element count to the current active level in the stack
                stack[-1][element] = stack[-1].get(element, 0) + count
            
            # ignores anything anonymmous
            else:
                i += 1

        return stack[0]

    # Unpack the reactants and products lists
    reactants, products = eq_seperator

    # Convert every molecule string into a dictionary of atom counts
    reactant_dicts = [parse_molecule(mol) for mol in reactants]
    product_dicts = [parse_molecule(mol) for mol in products]

    return reactant_dicts, product_dicts

if __name__ == '__main__':
    print(molecule_parser((['CO2', 'H2O'], ['C6H12O6', 'O2'])))

# CO2+H2O->C6H12O6+O2
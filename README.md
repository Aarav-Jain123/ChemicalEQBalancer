# Chemical Equation Balancer (Python)

A Python project that balances chemical equations using two different approaches:

1. **Randomized brute-force search** using `randint`
2. **Linear algebra solution** using `SymPy`

The program works with molecules represented as **element-count dictionaries** produced by a molecule parser.

---

# Example Reaction

Unbalanced reaction:

CO₂ + H₂O → C₆H₁₂O₆ + O₂

Balanced reaction:

6CO₂ + 6H₂O → C₆H₁₂O₆ + 6O₂

---

# Input Format

The balancer expects a tuple containing:

```
([reactants], [products])
```

Each molecule is represented as a dictionary:

```
element → number of atoms
```

Example:

```
(
[{'C':1,'O':2}, {'H':2,'O':1}],
[{'C':6,'H':12,'O':6}, {'O':2}]
)
```

Which represents:

```
CO2 + H2O → C6H12O6 + O2
```

---

# Algorithm 1: Random Brute Force

This method randomly generates coefficients for each compound until the equation balances.

Example idea:

```
aCO2 + bH2O → cC6H12O6 + dO2
```

Random values for `a, b, c, d` are generated using:

```
randint(1,10)
```

The program then checks whether:

```
atoms_left == atoms_right
```

If not, it tries again.

### Advantages

* Simple to understand
* Easy to implement
* Good learning exercise

### Disadvantages

* Not guaranteed to find a solution quickly
* May loop many times
* Fails if coefficients exceed the random range

---

# Algorithm 2: Linear Algebra (SymPy)

This method converts the balancing problem into a **matrix equation**.

For each element we write a balance equation.

Example for:

```
CO2 + H2O → C6H12O6 + O2
```

Matrix form:

```
[ 1  0 -6  0 ]
[ 0  2 -12 0 ]
[ 2  1 -6 -2 ]
```

Where:

* rows = elements
* columns = molecules

The system is solved using:

```
A · x = 0
```

SymPy computes the **nullspace** of the matrix, giving the correct coefficient ratios.

Example solution:

```
[6, 6, 1, 6]
```

---

# Features

* balances chemical equations
* supports arbitrary molecules
* uses dictionary-based molecular representation
* demonstrates two different algorithmic approaches

---

# Dependencies

Python libraries used:

```
random
math
functools
sympy
```

Install SymPy:

```
pip install sympy
```

---

# Example Usage

```
eq = (
[{'C':1,'O':2}, {'H':2,'O':1}],
[{'C':6,'H':12,'O':6}, {'O':2}]
)

print(balance(eq))
```

Output:

```
6CO2 + 6H2O = C6H12O6 + 6O2
```

---

# What This Project Demonstrates

* dictionary-based data modeling
* algorithm design
* brute-force search
* linear algebra applications
* symbolic mathematics with SymPy

---

# Possible Improvements

* handle nested parentheses
* add reaction verification
* improve brute-force search efficiency

---

# License

MIT

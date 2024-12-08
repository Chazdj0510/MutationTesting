# MutationTesting

## Introduction
Mutation testing evaluates the effectiveness of a test suite by introducing small modifications (mutations) to the code and checking whether the test suite can detect them. This process ensures robust test cases and identifies weaknesses in the test suite. The goal is to generate mutant versions of the `Polynomial` class, test them, and refine the test suite for maximum fault detection.

## List of Defined Mutation Operators
### Mutation Operators
1. Change Coefficients
    - Modify a coefficient value in the polynomial.
    - Example: [3, 0, 2] → [3, 1, 2]

2. Modify Arithmetic Operations
    - Replace one arithmetic operation (+, -, *, etc.) with another.
    - Example: Change addition in __add__ to subtraction.

3. Introduce Redundant Code
    - Add redundant statements or operations that do not affect functionality.
    - Example: Insert x = x + 0.

4. Remove Functionality
    - Remove key parts of a method.
    - Example: Omit the evaluation logic in evaluate.

5. Change Loop Logic
    - Alter loop conditions or iteration logic.
    - Example: Replace for i in range(...) with for i in range(... - 1).

6. Alter Conditional Statements
    - Modify conditions in if or for statements.
    - Example: Change if coef == 0: to if coef != 0:.

7. Swap Indexing
    - Change indexing order in lists.
    - Example: Reverse the list in __str__ method.

8. Alter Default Values
    - Change default parameter values.
    - Example: Change epsilon=1e-6 to epsilon=1e-3 in find_root_bisection.
  
## Applied Mutations

## Results

## Test Suite Effectiveness

## Recommendations

## Conclusion

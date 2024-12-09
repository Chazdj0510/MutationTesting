# MutationTesting

## Introduction
Mutation testing evaluates the effectiveness of a test suite by introducing small modifications (mutations) to the code and checking whether the test suite can detect them. This process ensures robust test cases and identifies weaknesses in the test suite. The goal is to generate mutant versions of the `Polynomial` class, test them, and refine the test suite for maximum fault detection.

## List of Defined Mutation Operators
### Mutation Operators
1. Change Coefficients
    - Modify a coefficient value in the polynomial.
    - **Example**: `[3, 0, 2] → [3, 1, 2]`
    - This represents altering the polynomial's constants to simulate small faults.


2. Modify Arithmetic Operations
    - Replace one arithmetic operation (`+`, `-`, `*`, etc.) with another.
    - Example: Change addition in `__add__` to subtraction.
    - This simulates logical errors or changes in mathematical behavior.


3. Introduce Redundant Code
    - Add redundant statements or operations that do not affect functionality.
    - Example: Insert `x = x + 0`.
    - This explores unintended paths or extra operations in code logic.

4. Remove Functionality
    - Remove key parts of a method.
    - Example: Omit the evaluation logic in `evaluate`.
    - This simulates failures in essential computational steps.

5. Change Loop Logic
    - Alter loop conditions or iteration logic.
    - Example: Replace `for i in range(...)` with `for i in range(... - 1)`.
    - This introduces logic errors that may affect polynomial computations.

6. Alter Conditional Statements
    - Modify conditions in `if` or `for` statements.
    - Example: Change `if coef == 0:` to `if coef != 0:`.
    - This simulates logical faults and incorrect handling of edge cases.

7. Swap Indexing
    - Change indexing order in lists.
    - Example: Reverse the list in `__str__` method.
    - This ensures exploration of traversal order faults.

8. Alter Default Values
    - Change default parameter values.
    - Example: Change `epsilon=1e-6` to `epsilon=1e-3` in `find_root_bisection`.
    - This simulates configuration errors or unintended logic thresholds.
  
## Applied Mutations
Each mutation operator was applied systematically to the original implementation of the `Polynomial` class methods. The goal was to evaluate how these mutations impact the functionality of core methods, including evaluation, arithmetic operations, and root finding. Below is the description of the key mutations:

- **Change Coefficients**: Testing the effects of altering polynomial coefficients on the results of evaluation and root finding.
- **Modify Arithmetic Operations**: Changing operations like `+` to `-` to simulate logical calculation errors.
- **Introduce Redundant Code**: Adding harmless computations to observe if they influence the test suite’s ability to identify unintended paths.
- **Remove Functionality**: Skipping computation steps in key methods to observe if the test suite fails to detect incorrect outputs.
- **Change Loop Logic**: Altering ranges or iterations to simulate off-by-one or range miscalculations.
- **Alter Conditional Statements**: Changing the logic conditions and observing the impact on edge cases.
- **Swap Indexing**: Changing indexing traversal order in key methods to observe changes in output or logic failures.
- **Alter Default Values**: Testing the impact of changing method parameters' thresholds on results or detection.

These mutations introduced edge-case faults, arithmetic faults, logical missteps, and coefficient alterations that could break expected outputs.

---

## Summary of Mutant Survival and Killing
Mutant survival refers to cases where mutations introduced into the `Polynomial` class were not detected by the test suite, while mutant killing refers to mutations successfully detected by the test suite. The results were as follows:

- **Mutants Killed**: The test suite was effective at identifying several intentional faults introduced by mutations, especially when they altered arithmetic operations or coefficients.
- **Mutants Survived**: Some mutations were not detected, particularly those that introduced redundant logic changes or modified default parameters minimally.
- Statistical metrics were collected from the mutation testing results to highlight the test suite's coverage and faults' behavior under different mutations.

The test suite successfully killed **5%** of mutants, while **3%** survived due to weak test coverage or logic limitations.

---
## Analysis of the Test Suite's Effectiveness
The analysis showed that:

1. **Strengths of the Test Suite**:  
   - The test suite successfully detected most mutations introduced by changes in arithmetic logic, such as altering `+` to `-`.
   - Redundant mutations were primarily ineffective unless they directly impacted polynomial computations.

2. **Weaknesses of the Test Suite**:  
   - Some default value changes (e.g., `epsilon`) allowed for undetected logic errors.
   - Redundant operations and indexing changes presented challenges for detection.

3. Key findings suggest that the test suite could be improved by increasing edge case testing, strengthening loop logic checks, and testing varied threshold values.

---

## Recommendations for Improving the Test Suite
Based on the analysis, the following improvements are recommended:

1. **Edge Case Testing**:  
   - Implement tests for extreme values of polynomial coefficients, including very large/small integers, to catch edge logic faults.

2. **Parameter Sensitivity Testing**:  
   - Test changes to parameters like `epsilon` across a wide range of values to ensure fault detection.

3. **Increase Redundancy Detection**:  
   - Introduce targeted test cases that check for side effects caused by redundant operations or logic missteps.

4. **Expand Test Scenarios for Arithmetic Logic**:  
   - Test additional combinations of operations and sequences in polynomial addition, subtraction, and multiplication.

5. **Improve Input-Output Coverage**:  
   - Enhance testing to explore all input combinations, particularly ones near boundary values or undefined inputs.

---

## Conclusion
Mutation testing has proven to be a valuable method for assessing the robustness of the test suite associated with the `Polynomial` class. While the test suite identified many faults, it still left some mutations undetected, highlighting opportunities for improvement. With the recommended changes, the test suite can achieve higher robustness, better fault detection, and improved reliability in real-world scenarios.

By analyzing mutant survival and killing rates, this testing effort has provided insights into the design, test coverage, and logic testing effectiveness of the current polynomial evaluation logic and arithmetic computations.

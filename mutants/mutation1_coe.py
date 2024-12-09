# mutation_change_coefficient.py

from Polynomial import Polynomial


class MutatedPolynomial(Polynomial):
    def __init__(self, coefficients):
        # Change coefficient at index 1 from its original value to 1
        mutated_coefficients = coefficients[:]
        if len(mutated_coefficients) > 1:
            mutated_coefficients[1] = 1
        super().__init__(mutated_coefficients)

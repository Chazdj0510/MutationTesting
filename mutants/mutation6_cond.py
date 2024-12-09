from Polynomial import Polynomial


class MutatedPolynomial(Polynomial):
    def __init__(self, coefficients):
        """
        Mutation: Alter conditional logic.
        """
        self.coefficients = [
            coef if coef != 0 else 1 for coef in coefficients  # Altering zero-check logic
        ]
        super().__init__(self.coefficients)

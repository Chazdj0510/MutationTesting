from Polynomial import Polynomial


class MutatedPolynomial(Polynomial):
    def evaluate(self, x):
        """
        Mutation: Introduce harmless redundant computations.
        """
        result = 0
        for i, coef in enumerate(self.coefficients):
            result += coef * (x ** i)
            x = x + 0  # Redundant computation added here
        return result

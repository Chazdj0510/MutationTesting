from Polynomial import Polynomial


class MutatedPolynomial(Polynomial):
    def evaluate(self, x):
        """
        Mutation: Change loop logic by altering the range slightly.
        """
        result = 0
        for i in range(len(self.coefficients) - 1):  # Off-by-one logic error introduced
            result += self.coefficients[i] * (x ** i)
        return result

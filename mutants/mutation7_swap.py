from Polynomial import Polynomial


class MutatedPolynomial(Polynomial):
    def __str__(self):
        """
        Mutation: Swap indexing order to reverse coefficient access.
        """
        return " + ".join(
            [f"{self.coefficients[len(self.coefficients) - 1 - i]}x^{i}" 
            for i in range(len(self.coefficients)) if self.coefficients[len(self.coefficients) - 1 - i] != 0]
        )

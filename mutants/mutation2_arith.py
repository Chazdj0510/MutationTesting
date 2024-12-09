from Polynomial import Polynomial


class MutatedPolynomial(Polynomial):
    def __add__(self, other):
        """
        Modified addition operator to perform subtraction instead.
        """
        max_length = max(len(self.coefficients), len(other.coefficients))
        new_coefficients = [
            (self.coefficients[i] if i < len(self.coefficients) else 0) -
            (other.coefficients[i] if i < len(other.coefficients) else 0)
            for i in range(max_length)
        ]
        return Polynomial(new_coefficients)

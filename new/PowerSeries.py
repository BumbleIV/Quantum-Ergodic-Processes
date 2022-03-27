from pip import main
from sympy import series, Symbol, sympify, Poly
from sympy.abc import x
import numpy as np


def main():
    # find coefficients of a power series

    # define a power series
    f0 = 1 + x + x ^ 2 + x ^ 3 + x ^ 4 + x ^ 5 + \
        x ^ 6 + x ^ 7 + x ^ 8 + x ^ 9 + x ^ 10

    # convert the power series to a polynomial
    f1 = Poly(f0, x)

    # find the coefficients of the polynomial
    coeff = f1.all_coeffs()
    print(coeff)


if __name__ == '__main__':
    main()

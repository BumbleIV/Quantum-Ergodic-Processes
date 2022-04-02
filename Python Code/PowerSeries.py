from pip import main
from sympy import series, Symbol, sympify, Poly, cos, sin, tan, oo
from sympy.abc import a, n, s, x, y, z
import numpy as np


def main():
    """ 
    parameters of series(expr, x, x0, n, dir)
    expr: expression to be evaluated
    x: variable to be evaluated
    x0: initial value of x
    n: number of terms to be evaluated
    dir: direction of evaluation
    """

    # example series
    f = a * s ** n

    print("\nExample Series:")
    series_f1 = series(f, s, 0, 10, "+")
    print(series_f1)

    coeff = series_f1.all_coeffs()

    print("\nCoefficients:")
    print(coeff)

    # # our power series
    # x0 = 0
    # n = 10
    # f = a * s ** n

    # print("\nOur power series:")
    # print(series(a * s**n, s, x0, n, "+"))


if __name__ == '__main__':
    main()

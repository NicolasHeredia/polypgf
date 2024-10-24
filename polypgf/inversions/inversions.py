from math import factorial
import numpy as np
from typing import Callable, List

def Kn(n: int, N: int) -> float:
    """Parameter Kn of Stehfest method.

    Parameters
    ----------
    n : int
        Index of K.
    N : int
        N must be even.

    Returns
    -------
    float
        Value of parameter K in index n.
    """
    sumatoria = 0.0
    lw = int((n + 1) / 2)
    up = int(min(n, N / 2))
    for k in range(lw, up + 1):
        numerador = (k ** (N / 2) * factorial(2 * k))
        denominador = (
            factorial(int(N / 2) - k)
            * factorial(k)
            * factorial(k - 1)
            * factorial(n - k)
            * factorial(2 * k - n)
        )
        sumatoria += numerador / denominador
    K_n = (-1) ** (n + N / 2) * sumatoria

    return K_n

def stehfest(
    N: int, 
    DP: List[float], 
    t: float, 
    func: Callable[[float, float], List[float]], 
    pos: int
) -> List[float]:
    """Stehfest method.

    Parameters
    ----------
    N : int
        N must be even.
    DP : List[float]
        Degree of polymerization.
    t : float
        Time at which to evaluate the PGF.
    func : Callable[[float, float], List[float]]
        Mass balances function.
    pos : int
        Position of PGF in the solution of the mass balances.

    Returns
    -------
    List[float]
        Molecular weight distribution (MWD).
    """
    resultados_f_x = []

    for x in DP:
        sumatoria = 0.0
        for n in range(1, N + 1):
            K_n = Kn(n, N)
            z = np.exp(-n * np.log(2) / x)

            # Auxiliary calculations to obtain the pgf
            pgf = func(z, t)[pos]

            sumatoria += K_n * pgf
        f_x = (np.log(2) / x) * sumatoria
        resultados_f_x.append(f_x)

    return resultados_f_x

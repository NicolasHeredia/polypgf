from typing import Optional, Union

import numpy as np


class KineticArrhenius:
    def __init__(
        self,
        *,
        name: str,
        Ea: Union[int, float],
        A: Optional[Union[int, float]] = None,
        k_ref: Optional[Union[int, float]] = None,
        T_ref: Optional[Union[int, float]] = None,
        R: float = 8.314,
    ):

        self.name: str = name
        self.Ea: Union[int, float] = Ea
        self.A: Optional[Union[int, float]] = A
        self.k_ref: Optional[Union[int, float]] = k_ref
        self.T_ref: Optional[Union[int, float]] = T_ref
        self.R: float = R

    def __repr__(self) -> str:
        return (
            f"Kinetic Constant Arrhenius\n"
            f"{'-'*30}\n"
            f"name = {self.name}\n"
            f"A  = {self.A}\n"
            f"Ea = {self.Ea} J/mol\n"
            f"R  = {self.R} J/mol·K\n"
        )

    def value(self, T: Union[int, float]) -> float:
        if self.A is not None:
            return self.A * np.exp(-self.Ea / (self.R * T))
        elif self.k_ref is not None and self.T_ref is not None:
            return self.k_ref * np.exp(
                -(self.Ea / self.R) * ((1 / self.T_ref) - (1 / T))
            )
        else:
            raise ValueError(
                "Either 'A' or both 'k_ref' " "and 'T_ref' must be provided."
            )

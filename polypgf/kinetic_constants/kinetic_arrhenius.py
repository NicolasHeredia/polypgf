import numpy as np
class KineticArrhenius:
    def __init__(self, A, Ea, name, R=8.314):
        self.A = A
        self.Ea = Ea
        self.name = name
        self.R = R


    def __repr__(self):
        return (f"Kinetic Constant Arrhenius\n"
                f"{'-'*30}\n"
                f"name = {self.name}\n"
                f"A  = {self.A}\n"
                f"Ea = {self.Ea} J/mol\n"
                f"R  = {self.R} J/mol·K\n")
    
    def value(self,  T):
        return self.A * np.exp(-self.Ea / (self.R * T))

    
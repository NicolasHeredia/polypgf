class KineticIsothermal:
    def __init__(self, k, T, name):
        self.k = k
        self.T = T
        self.name = name

    def __repr__(self):
        return (
            f"Kinetic Constant Isothermal\n"
            f"{'-'*30}\n"
            f"name = {self.name}\n"
            f"k  = {self.k}\n"
            f"T = {self.T} K\n"
        )

    def value(self):
        return self.k

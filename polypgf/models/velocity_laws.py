import numpy as np
from polypgf.kinetic_constants.kinetic_arrhenius import KineticArrhenius
from polypgf.thermo.ideal_solution import IdealSolution

class Reactions(KineticArrhenius, IdealSolution):

    def __init__(self, ):

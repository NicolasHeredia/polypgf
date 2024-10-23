import numpy as np
from polypgf.kinetic_constants.kinetic_arrhenius import KineticArrhenius
from polypgf.thermo.ideal_solution import IdealSolution
from dataclasses import dataclass
from typing import float64, Union

@dataclass
class Reactions:

    descomposition = 'descomposition'
    initiation = 'initiation'
    propagation = 'propagation'
    termination_comb = 'termination_combination'
    termination_desp = 'termination_desproportion'
    monomer_transfer = 'monomer_transfer'
    solvent_transfer = 'solvent_transfer'




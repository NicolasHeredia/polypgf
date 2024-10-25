# import numpy as np
# from polypgf.kinetic_constants.kinetic_arrhenius import KineticArrhenius
# from polypgf.thermo.ideal_solution import IdealSolution
from dataclasses import dataclass

# from typing import float64, Union


@dataclass
class ReactionType:

    descomposition = "descomposition"
    initiation = "initiation"
    propagation = "propagation"
    termination_comb = "termination_combination"
    termination_desp = "termination_desproportion"
    monomer_transfer = "monomer_transfer"
    solvent_transfer = "solvent_transfer"

    def _moles(N, V):
        return N / V


REACTION_SPECS = {
    ReactionType.descomposition: {
        "reactants": {"I": 1},
        "products": {"radicals": 1},
        "rate_equation": lambda k, conc: k * conc["I"]
    },
    ReactionType.initiation: {
        "reactants": {"I": 1},
        "products": {"radicals": 1},
        "rate_equation": lambda k, f, conc: 2 * f * k * conc["I"],
    },
    ReactionType.propagation: {
        "reactants": {"M": 1, "Y0": 1},
        "products": {"radicals"},
        "rate_equation": lambda k, conc: k * conc["M"] * conc["Y0"],
    },
    ReactionType.termination_comb: {
        "reactants": {"Y0": 1},
        "products": {"polymer": 1},
        "rate_equation": lambda k, conc: k * (conc["Y0"])**2,
    },
    ReactionType.termination_desp: {
        "reactants": {"Y0": 1},
        "products": {"polymer": 1},
        "rate_equation": lambda k, conc: k * conc["Y0"],
    },
    ReactionType.monomer_transfer: {
        "reactants": {"M": 1, "Y0": 1},
        "products": {"radicals": 1, "polymer": 1},
        "rate_equation": lambda k, conc: k * conc["M"] * conc["Y0"],
    },
    ReactionType.solvent_transfer: {
        "reactants": {"S": 1, "Y0": 1},
        "products": {"radicals": 1, "polymer": 1},
        "rate_equation": lambda k, conc: k * conc["S"] * conc["Y0"],
    },
}



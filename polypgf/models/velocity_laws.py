import numpy as np
from polypgf.kinetic_constants.kinetic_arrhenius import KineticArrhenius
from polypgf.thermo.ideal_solution import IdealSolution
from dataclasses import dataclass
from typing import float64, Union

@dataclass
class ReactionType:

    descomposition = 'descomposition'
    initiation = 'initiation'
    propagation = 'propagation'
    termination_comb = 'termination_combination'
    termination_desp = 'termination_desproportion'
    monomer_transfer = 'monomer_transfer'
    solvent_transfer = 'solvent_transfer'

    def _moles(N, V):
        return N / V

REACTION_SPECS = {
    ReactionType.descomposition: {
        'reactants': {'I': 1},
        'products': {},
        'rate_equation': lambda k, conc: k * conc['A'] * conc['O2']
    },
    ReactionType.initiation: {
        'reactants': {'A': 1, 'H2O': 1},
        'products': {'B': 1, 'C': 1},
        'rate_equation': lambda k, conc: k * conc['A'] * conc['H2O'],
        'delta_H': -50.0
    },
    ReactionType.propagation: {
        'reactants': {'A': 1},
        'products': {'B': 1},
        'rate_equation': lambda k, conc: k * conc['A'],
        'delta_H': 30.0
    },
    ReactionType.termination_comb: {
        'reactants': {'A': 1},
        'products': {'B': 1, 'C': 1},
        'rate_equation': lambda k, conc: k * conc['A'],
        'delta_H': 45.0
    },
    ReactionType.termination_desp: {
        'reactants': {'A': 1, 'B': 1},
        'products': {'C': 1},
        'rate_equation': lambda k, conc: k * conc['A'] * conc['B'],
        'delta_H': -85.0
    },
    ReactionType.monomer_transfer: {
        'reactants': {'A': 1, 'B': 1},
        'products': {'C': 1},
        'rate_equation': lambda k, conc: k * conc['A'] * conc['B'],
        'delta_H': -85.0
    },
    ReactionType.solvent_transfer: {
        'reactants': {'A': 1, 'B': 1},
        'products': {'C': 1},
        'rate_equation': lambda k, conc: k * conc['A'] * conc['B'],
        'delta_H': -85.0
    }
}

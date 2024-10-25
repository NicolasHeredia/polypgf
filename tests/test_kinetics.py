import numpy as np

from polypgf.kinetic_constants.kinetic_arrhenius import KineticArrhenius

import pytest


@pytest.fixture
def kinetic_with_A():
    return KineticArrhenius(
        name="Reaction1", Ea=50000, A=1e12, k_ref=None, T_ref=None
    )


@pytest.fixture
def kinetic_with_kref():
    return KineticArrhenius(
        name="Reaction2", Ea=60000, A=None, k_ref=1e5, T_ref=298
    )


def test_repr(kinetic_with_A):
    expected_repr = (
        "Kinetic Constant Arrhenius\n"
        + "-" * 30
        + "\n"
        + "name = Reaction1\n"
        + "A  = 1000000000000.0\n"
        + "Ea = 50000 J/mol\n"
        + "R  = 8.314 J/mol·K\n"
    )
    assert repr(kinetic_with_A) == expected_repr


def test_value_with_A(kinetic_with_A):
    T = 350  # Temperatura en K
    expected_value = kinetic_with_A.A * np.exp(
        -kinetic_with_A.Ea / (kinetic_with_A.R * T)
    )
    assert pytest.approx(kinetic_with_A.value(T), 0.00001) == expected_value


def test_value_with_kref(kinetic_with_kref):
    T = 350  # Temperatura en K
    expected_value = kinetic_with_kref.k_ref * np.exp(
        -(kinetic_with_kref.Ea / kinetic_with_kref.R)
        * ((1 / kinetic_with_kref.T_ref) - (1 / T))
    )
    assert pytest.approx(kinetic_with_kref.value(T), 0.00001) == expected_value


def test_value_raises_error():
    kinetic_invalid = KineticArrhenius(
        name="Invalid", Ea=60000, A=None, k_ref=None, T_ref=None
    )
    with pytest.raises(
        ValueError,
        match="Either 'A' or both 'k_ref' and 'T_ref' must be provided.",
    ):
        kinetic_invalid.value(350)

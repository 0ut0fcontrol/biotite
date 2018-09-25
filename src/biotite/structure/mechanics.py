# This source code is part of the Biotite package and is distributed
# under the 3-Clause BSD License. Please see 'LICENSE.rst' for further
# information.

"""
This module provides functions for calculation of mechanical or
mass-related properties of a molecular structure.
"""

__author__ = "Patrick Kunzmann"
__all__ = ["mass_center", "gyration_radius"]

import numpy as np
from .atoms import Atom, AtomArray, AtomArrayStack, coord
from .util import vector_dot, norm_vector
from .error import BadStructureError
from .geometry import distance
from .info.atoms import atom_masses


def gyration_radius(array, masses=None):
    """
    Compute the radius/radii of gyration of an atom array or stack.
    
    Parameters
    ----------
    array : AtomArray or AtomArrayStack
        The array or stack to calculate the radius/radii of gyration
        for.
    masses : ndarray, optional
        The masses to use for each atom in the input `array`.
        Must have the same length as `array`. By default, the standard
        atomic mass for each element is taken.
    
    Returns
    -------
    masses : float or ndarray, dtype=float
        If `array` is an `AtomArray`, the radius of gyration is
        returned as single float.
        If `array` is an `AtomArrayStack`, an `ndarray` containing the
        radii of gyration for every model is returned.
    """
    center = mass_center(array, masses)
    radii = distance(array, center[..., np.newaxis, :])
    inertia_moment = np.sum(masses * radii*radii, axis=-1)
    return np.sqrt(inertia_moment / np.sum(masses))

def mass_center(array, masses=None):
    """
    Calculate the center(s) of mass of an atom array or stack.
    
    Parameters
    ----------
    array : AtomArray or AtomArrayStack
        The array or stack to calculate the center(s) of mass for.
    masses : ndarray, optional
        The masses to use for each atom in the input `array`.
        Must have the same length as `array`. By default, the standard
        atomic mass for each element is taken.
    
    Returns
    -------
    radius : ndarray, ndarray, dtype=float
        Array containing the the coordinates of the center of mass.
        If `array` is an `AtomArray`, this will be an length 3
        `ndarray`; if it is an `AtomArrayStack` with *n* models,
        a (*n x 3*) `ndarray` is returned.
    """
    if masses is None:
        masses = np.zeros(array.array_length())
        for i, element in enumerate(array.element):
            try:
                masses[i] = atom_masses[element]
            except KeyError:
                raise ValueError(f"'{element}' is not a valid element")
    return np.sum(masses[:,np.newaxis] * array.coord, axis=-2) / np.sum(masses)
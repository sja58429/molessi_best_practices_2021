"""
molecool
A Python package for analyzing and visulazing molecular files. For molssi workshop.
"""

# Add imports here
from .functions import canvas, zen
from .measure import calculate_angle, calculate_distance
from .molecule import build_bond_list
from .visulize import draw_molecule, bond_histogram
from .molecule import calculate_distance, calculate_molecular_mass, calculate_center_of_mass
import io

# Handle versioneer
from ._version import get_versions
versions = get_versions()
__version__ = versions['version']
__git_revision__ = versions['full-revisionid']
del get_versions, versions

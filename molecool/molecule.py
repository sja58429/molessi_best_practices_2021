"""
Functions to measure molecules 
"""
import numpy as np 
import math 
#from the measure module import calculate_distance function 
# . means look at the current working directory 
from abc import abstractstaticmethod

from numpy import core
from .measure import calculate_distance 
from .atom_data import atomic_weights
from molecool import atom_data

def build_bond_list(coordinates, max_bond=1.5, min_bond=0):
    
    # Find the bonds in a molecule (set of coordinates) based on distance criteria.
    bonds = {}
    num_atoms = len(coordinates)

    for atom1 in range(num_atoms):
        for atom2 in range(atom1, num_atoms):
            distance = calculate_distance(coordinates[atom1], coordinates[atom2])
            if distance > min_bond and distance < max_bond:
                bonds[(atom1, atom2)] = distance

    return bonds
    

def calculate_molecular_mass(symbols):
    total_mass = 0
        
    for atom in symbols:
        total_mass  += atomic_weights.get(atom)
        
    return total_mass 


def calculate_center_of_mass(symbols, coordinates):
    
    sum = 0 
    total_mass = calculate_molecular_mass(symbols)
    atom_weight = []
    
    atom_weight = [atomic_weights.get(atom) for atom in symbols]
    
    adjusted_coord = [atom_weight[i]* coordinates[i] for i in range(len(symbols))]
    
    sum_array = 0 
    for i in range(len(adjusted_coord)):
        sum_array += adjusted_coord[i]
        
    center_mass = (1/total_mass)*sum_array
            
    print(center_mass)    
    return center_mass
     



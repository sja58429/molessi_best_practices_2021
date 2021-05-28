"""
Tests for measure module
"""
import numpy as np 
import molecool
import pytest 
def test_molecular_mass():
    symbols = ['C', 'H', 'H', 'H', 'H']
    calculated_mass = molecool.calculate_molecular_mass(symbols)
    actual_mass = 16.04
    
    assert pytest.approx(actual_mass, abs=1e-2) == calculated_mass
    
    
def test_center_of_mass():
    symbols = np.array(['C', 'H', 'H', 'H', 'H'])
    coordinates = np.array([[1,1,1], [2.4,1,1], [-0.4, 1, 1], [1, 1, 2.4], [1, 1, -0.4]])
    center_of_mass = molecool.calculate_center_of_mass(symbols, coordinates)
    expected_center = np.array([1,1,1])
    12.01
    assert np.array_equal(expected_center, center_of_mass)
    
    
    
def test_calculate_angle():
    r1 = np.array([0,0,-1])
    r2 = np.array([0,0,0])
    r3 = np.array([1,0,0])
    
    expected_angle = 90 

    calculate_angle = molecool.calculate_angle(r1,r2,r3, degrees=True)
    
    assert expected_angle == calculate_angle 
    
    
def test_calculate_distance():
    """Test: that calculate_distance what we expect"""
    r1 = np.array([0,0,0])
    r2 = np.array([0,1,0])
    
    expected_distance = 1
    
    calculate_distance = molecool.calculate_distance(r1,r2)
    
    assert expected_distance == calculate_distance
    
# this will skip the test 
@pytest.mark.skip 
def test_calculate_angle_60():
    r1 = np.array([0,0,-1])
    r2 = np.array([0,1,0])
    r3 = np.array([1,0,0])
    
    expected_angle = 60
    
    calculate_angle = molecool.calculate_angle(r1, r2, r3, degrees= True)

    assert pytest.approx(expected_angle) == calculate_angle

@pytest.mark.parametrize("r1, r2, r3, expected_angle", [
    ( np.array([0,0,-1]), np.array([0,0,0]), np.array([1,0,0]),90),
    (np.array([0,0,-1]), np.array([0,1,0]), np.array([1,0,0]),60 ),
])
def test_calculate_angle_many(r1,r2,r3, expected_angle):
    calculate_angle = molecool.calculate_angle(r1,r2,r3, degrees = True)
    assert pytest.approx(calculate_angle) == expected_angle 
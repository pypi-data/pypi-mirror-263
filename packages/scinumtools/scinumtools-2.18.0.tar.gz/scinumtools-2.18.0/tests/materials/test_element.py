import numpy as np
import pytest
from math import isclose
import os
import sys
sys.path.insert(0, 'src')

from scinumtools.units import Quantity, Unit 
from scinumtools.materials import *

def test_expression():
    
    # Natural abundance
    e = Element('B')
    assert str([e.mass,e.Z,e.N,e.e]) == "[Quantity(1.081e+01 Da), 5.0, 5.801, 5.0]"
    assert isclose(e.mass.value(), 10.811028046410001, rel_tol=MAGNITUDE_PRECISION)
    
    # Isotope
    e = Element('B{11}')
    assert str([e.mass,e.Z,e.N,e.e]) == "[Quantity(1.101e+01 Da), 5, 6, 5]"
    assert isclose(e.mass.value(), 11.009306, rel_tol=MAGNITUDE_PRECISION)

    # Isotope and ionisation
    e = Element('B{11-1}')
    assert str([e.mass,e.Z,e.N,e.e]) == "[Quantity(1.101e+01 Da), 5, 6, 4]"
    assert isclose(e.mass.value(), 11.008757420144217, rel_tol=MAGNITUDE_PRECISION)

    # Most abundant
    e = Element('B', natural=False)
    assert str([e.mass,e.Z,e.N,e.e]) == "[Quantity(1.101e+01 Da), 5, 6, 5]"
    assert isclose(e.mass.value(), 11.009306, rel_tol=MAGNITUDE_PRECISION)
    

def test_print():
    
    e = Element('O')
    assert str(e) == "Element(O mass=15.999 Z=8.0 N=8.004 e=8.0)"
    assert str((e.Z, e.N, e.e, e.mass)) == "(8.0, 8.00448, 8.0, Quantity(1.600e+01 Da))"

    e = Element('O', natural=False)
    assert str(e) == "Element(O mass=15.995 Z=8 N=8.000 e=8)"
    
    e = Element('O', count=2, natural=False)
    assert str(e) == "Element(O2 mass=31.990 Z=16 N=16.000 e=16)"
    assert e.count == 2
    assert e.element == 'O'
    assert e.isotope == 16
    assert e.ionisation == 0
    
    e = Element('O{17-2}')
    assert str(e) == "Element(O{17-2} mass=16.998 Z=8 N=9.000 e=6)"

def test_arithmetic():
    
    e1 = Element('B')
    e2 = Element('B',2)

    # addition
    e12 = e1 + e2
    assert e12.count == e1.count + e2.count

    # multiplication
    e13 = e1 * 3
    assert e13.count == e1.count * 3

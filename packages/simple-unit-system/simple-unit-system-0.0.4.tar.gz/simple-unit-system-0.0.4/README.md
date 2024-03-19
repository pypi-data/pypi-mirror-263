# Python Physical Unit System Framework
A physical units framework for scientific and engineering programming

This implementation of a units framework for python, has low overhead, and can be expanded upon as desired.
Reference conversion factors and constants are derived from NIST standards when available
Some US customary units use implicit conversions and derivations

## Use:

**import the library and establish the base unit system**

from units import units
C = units('US')

**assign units to a number - in this case 10 lbf of force:**

F = 10*C.LBF

**report the number in units force:**

print( F/C.LBF )

**report the number in units of Newtons:**

print ( F/C.N )

**assign a mixed unit to a value in this case density in SI units:**

rho = 10 *C.KG/C.M**3

**report the unit is US customary units:**

print ( rho / (C.SLUG/C.FT**3) )

#from ASE.ChemicalElements.ChemicalElements import Element, numbers
import crystalIO
import atomic_properties

def atom( *args ):
    """create an atom

    atom( 26, 57 )
    atom( 26 )
    atom( 'Fe' )
    atom( 'Fe', 57 )
    """
    if len(args) == 1:
        Z = args[0]
        A = None
    elif len(args) == 2:
        Z, A = args
    else:
        raise RuntimeError , "Unable to create an atom from %s" % ( args, )
    
    if isinstance( Z, basestring):
        symbol = Z
        Z = None
    else:
        symbol = None
        pass

    return Atom( Z = Z, symbol = symbol, mass = A )

from matter.StructureErrors import *
from matter.Atom import Atom
from matter.Lattice import Lattice
from matter.Structure import Structure

# obtain version information
from matter.version import __version__
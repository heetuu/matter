# -*- Python -*-
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#                                   Jiao Lin
#                      California Institute of Technology
#                      (C) 2006-2009  All Rights Reserved
#
# {LicenseText}
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#


from dsaw.model.Inventory import Inventory as InvBase


# data object
from Atom import Atom
from Lattice import Lattice
from UnitCell import UnitCell
from matter.Structure import Structure


# inventory
from dsaw.model.Inventory import Inventory as InvBase
class Inventory(InvBase):

    short_description = InvBase.d.str(
        name = 'short_description', max_length = 256, default ="", label='Description')
    lattice = InvBase.d.reference(name = 'lattice', targettype=Lattice, owned=1)
    atoms = InvBase.d.referenceSet(name='atoms', targettype=Atom, owned=1)
    spacegroupno = InvBase.d.int(name = 'spacegroupno', default =1, label='Spacegroup #')
    chemical_formula = InvBase.d.str(name='chemical_formula', max_length=1024)
    primitive_unitcell = InvBase.d.reference(
        name='primitive_unitcell', targettype=UnitCell, owned=1)
    date = InvBase.d.date(name='date')

    dbtablename = 'atomicstructures'

Structure.Inventory = Inventory


# dsaw.model helpers
def __establishInventory__(self, inventory):
    inventory.short_description = self.description
    inventory.lattice = self.lattice
    inventory.spacegroupno = self.sg.number
    inventory.chemical_formula = self.getChemicalFormula()
    inventory.atoms = list(self) # the implementation of Structure class is that structure is inherited from list, and the items are atoms.
    inventory.primitive_unitcell = self.primitive_unitcell
    return
Structure.__establishInventory__ = __establishInventory__

def __restoreFromInventory__(self, inventory):
    self.__init__(atoms=inventory.atoms,
                  lattice=inventory.lattice,
                  sgid=inventory.spacegroupno,
                  description=inventory.short_description,
                  )
    self.primitive_unitcell = inventory.primitive_unitcell
    return
Structure.__restoreFromInventory__ = __restoreFromInventory__


# version
__id__ = "$Id$"

# End of file 

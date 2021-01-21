

import numpy as np
from megnet.models import MEGNetModel
from megnet.data.crystal import CrystalGraph
from pymatgen import Lattice
from pymatgen import Structure

class GapPredict():
  def _init_(self,model,lattice,species_list,system,positions_list):
    self.model = model
    self.lattice = lattice
    self.species_list = species_list
    self.system = system
    self.positions_list = positions_list
  
  def structure_generator(self):
    if(self.system == 'cubic'):
      structure = Structure(self.lattice,self.species_list,self.positions_list,coords_are_cartesian= False)
    if(self.system == 'orthorhombic'):
      structure = Structure(self.lattice,self.species_list,self.positions_list,coords_are_cartesian= False)
    else:
      structure = 0
    return structure
  
  def gapPredictor(self):
    structure = self.structure_generator()
    try:
      bandgap = model.predict_structure(structure)
    except:
      bandgap = 'nan'
    return bandgap

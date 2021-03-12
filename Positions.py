# -*- coding: utf-8 -*-
class positions_species_list():
  def __init__(self,input_dict = {},tolerance = ''):
    self.input_dict = input_dict
    self.tolerance = tolerance

  def positions_species():  #assigns positions to ions based on crystal structure determined

    if (self.input_dict['A1'][1] == 'n' and self.input_dict['B1'][1] == 'n' and self.input_dict['C1'][1] == 'n'):     #condition to check whether or not it is a double perovskite
      if (self.tolerance == 'cubic'):
        species_list = [self.input_dict['A'][0],self.input_dict['B'][0],self.input_dict['C'][0],self.input_dict['C'][0],self.input_dict['C'][0]]
        positions_list = [(0,0,0),(0.5,0.5,0.5),(0.5,0,0.5),(0.5,0.5,0),(0,0.5,0.5)]    

      if (self.tolerance == 'orthorhombic'):
        species_list = [self.input_dict['A'][0] for i in range(4)] + [self.input_dict['B'][0] for i in range(4)] + [self.input_dict['C'][0] for i in range(12)]
        positions_list = [(0.5,0.5,0.75),(0.5,0.5,0.25),(1,0,0.75),(0,1,0.25),(0,0.5,0.5),(0,0.5,0),(0.5,0,0.5),(0.5,0,0),(0,0.5,0.75),(0,0.5,0.25),(0.5,1,0.75),(0.5,0,0.25),(0.75,0.75,1),(0.25,0.25,0.5),(0.25,0.25,0),(0.75,0.75,0.5),(0.75,0.25,1),(0.25,0.75,0.5),(0.25,0.75,0),(0.75,0.25,0.5)]

    else: #assigning positions of ions for double perovskites
      if (self.tolerance == 'cubic'):
        species_list = [self.input_dict['A'][0],self.input_dict['A1'][0],self.input_dict['B'][0],self.input_dict['B1'][0]] + [self.input_dict['C'][0] for i in range(6)] 
        positions = [(0.25,0.25,0.25),(0.75,0.75,0.75),(0,0,0,),(0.5,0.5,0.5),(0.25,0.25,0.75),(0.25,0.75,0.75),(0.25,0.5,0.25),(0.75,0.25,0.25),(0.75,0.25,0.75),(0.75,0.75,0.25)]

      if (self.tolerance == 'orthorhombic'):
        species_list = [self.input_dict['A'][0] for i in range(2)] + [self.input_dict['A1'][0] for i in range(2)] + [self.input_dict['B'][0] for i in range(2)] + [self.input_dict['B1'][0] for i in range(2)] + [self.input_dict['C'][0] for i in range(12)] 
        positions = [(0,0.75,0.5),(0,0.25,0.5),(0.5,0.25,0),(0.5,0.75,0),(0.5,0.5,0.5),(1,1,1)(0,0.5,0),(0.5,0,0.5),(0,0.25,0),(0,0.75,0),(0.25,0.5,0.25),(0.25,0.5,0.75),(0.25,0,0.25),(0.25,0,0.75),(0.5,0.75,0.5),(0.5,0.25,0.5),(0.75,0,0.75),(0.75,0,0.25),(0.75,0.5,0.75),(0.75,0.5,0.25)]
    
    return species_list,positions_list    #returns lists of ions and their positions in the structure

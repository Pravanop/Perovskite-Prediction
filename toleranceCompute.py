#This class is responsible for calculating the Goldschmidt tolerance factor and determining the crystal structure using the input ionic radii for elements at each site.
# Tolerance factor (t)                Structure
#       >1                      Hexagonal/Tetragonal
#      0.9-1                    Cubic
#     0.71-0.9                  Orthorhombic/Rhombohedral
#      <0.71                    Different structures

class tolerance_compute():
  def __init__(self,input_dict = {}):
    self.input_dict = input_dict
  
  def tolerance_compute(self):                    
    A_radius = self.inputs_dict['A'][1]             #Radius of ion at A site
    A1_radius = self.inputs_dict['A1'][1]           #Radius of 2nd ion at A site in case of a double perovskite
    B_radius = self.inputs_dict['B'][1]             #Radius of ion at B site
    B1_radius = self.inputs_dict['B1'][1]           #Radius of 2nd ion at B site in case of a double perovskite
    C_radius = self.inputs_dict['C'][1]             #Radius of ion at X site

    Aavg_radius = A_radius + A1_radius              #Sum of radii for double perovskites
    Bavg_radius = B_radius + B1_radius
    Cavg_radius = 2*C_radius 
    t = (Aavg_radius/2) + (Cavg_radius/2)
    t = t/ ((Bavg_radius/2) + (Cavg_radius/2))
    t = t/1.414                                     #Tolerance factor

    if ( t >= 0.813 and t < 1.017):
      return 'cubic'
    
    if (t >= 0.71 and t < 0.813):
      return 'orthorhombic'
    
    else:
      return 'invalid input'                        #accepting only cubic and orthorhombic structures

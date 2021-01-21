
class tolerance_compute():
  def __init__(self,input_dict = {}):
    self.input_dict = input_dict
  
  def tolerance_compute(self):
    A_radius = self.inputs_dict['A'][1]
    A1_radius = self.inputs_dict['A1'][1]
    B_radius = self.inputs_dict['B'][1]
    B1_radius = self.inputs_dict['B1'][1]
    C_radius = self.inputs_dict['C'][1]

    Aavg_radius = A_radius + A1_radius
    Bavg_radius = B_radius + B1_radius
    Cavg_radius = 2*C_radius 
    t = (Aavg_radius/2) + (Cavg_radius/2)
    t = t/ ((Bavg_radius/2) + (Cavg_radius/2))
    t = t/1.414

    if ( t >= 0.813 and t < 1.017):
      return 'cubic'
    
    if (t >= 0.71 and t < 0.813):
      return 'orthorhombic'
    
    else:
      return 'invalid input'

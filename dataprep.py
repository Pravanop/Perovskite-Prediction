import pymatgen.io.ase as aseconvert
from ase.db import connect
import numpy as np
import pandas as pd
from pymatgen.io.cif import CifWriter
import os

class DatasetPrep():

  def __init__(self, path_output = '', short_name = '' ):
        self.path_output = path_output
        self.short_name = short_name

  def ase_to_cif(self,path_input):
        db = connect(path_input) #loads in a ASE database
        pymat_struct_list = []
        for row in db.select():
            try:
              atoms = row.toatoms()   #converts to ASE Atoms object
              pymat_struct_indi = aseconvert.AseAtomsAdaptor.get_structure(atoms)  #converts to pymatgen Structure module
              pymat_struct_list.append(pymat_struct_indi)
            except:
              continue
        target_list = []
        for row in db.select():
            try:
              target_bandgap = row.GLLB_ind
              target_list.append(float(target_bandgap))
            except:
              target_list.append('nan')
              continue
        if(len(target_list) == len(pymat_struct_list)):
          for count,struct in enumerate(pymat_struct_list):
            w = CifWriter(struct)
            # writes a cif file into the output path
            # for example, cubic perovskites database: cp1.cif
            w.write_file(self.path_output + '/structures/' + self.short_name + str(count) + '.cif')
          id = []
          for count_target in range(len(target_list)):
            id.append(self.short_name + str(count_target))   #creating an id list

          target_dict = {'id' : id, 'targets' : target_list}
          target_df = pd.DataFrame(target_dict, index =[x for x in range(1,len(target_list)+1)])
          name = self.path_output + '/targets/' + self.short_name + '.csv'
          #creates a csv file with two columns, id and target_bandgap
          target_df.to_csv(name,index=False)
        else:
          print('Something is wrong! The list lengths are unequal!')
        return print('CIFs generated along with a .csv file of target bandgaps')

  def cif_to_cif(self,path_input):
    for count, filename in enumerate(os.listdir(path_input)):
        dst = self.short_name + str(count) + ".cif"
        src = path_input + '/' + filename
        dst = path_input + '/' + dst
        os.rename(src, dst)
    cif_file = os.listdir(path_input + '/')
    targets=[]
    for cif in cif_file:       #unfortunately hardcoded for the two datasets with target bandgaps noted in the comments of the cif file
      line_array=[]
      band_gaps=[]
      with open(path_input +'/' + cif,"r") as a_file:
        for line in a_file:
          stripped_line = line.strip()
          line_array.append(stripped_line)
        band_gaps.append(cif)
        for i in range(36,len(line_array)):
          if(line_array[i][:9] == '# Bandgap'):
            band_gaps.append(line_array[i][len(line_array[i])-6:])
      targets.append(band_gaps)
    for i in targets:  #cleaning targets
      if(i[1] != '    xx' and i[2] != '    xx'):
        i[1] = float(i[1])
        i[2] = float(i[2])
    target_df = pd.DataFrame(targets)
    target_df.columns = ['id','targets','aux']
    name = self.path_output + '/targets/' + self.short_name + '.csv'
    #creates a csv file with two columns, id and target_bandgap
    target_df.to_csv(name,index=False)
    return print('CIFs generated along with a .csv file of target bandgaps')

  def dataset_concatenator(self,path_input):
    combined_csv = pd.concat([pd.read_csv(f) for f in os.listdir(path_input)])
    combined_csv.to_csv( self.path_output + '/Targets_Final.csv', index=False, encoding='utf-8-sig')

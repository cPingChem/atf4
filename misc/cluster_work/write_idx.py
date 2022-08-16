import numpy as np
import sys
import subprocess
import argparse

idx = 13050 # There are 13050 atoms as indexed on the pdb file. 
parser = argparse.ArgumentParser()
parser.add_argument("i", help="trajectory index", type=int)

args = parser.parse_args()
i = args.i
traj_in  = 'traj_'+str(i)+'.h5'
traj_out  = 'traj_nw_'+str(i)+'.h5'
#traj_in  = f"traj_{i}.h5"
#traj_out = f"traj_{i}.pdb"

indeces= ' '.join((str(x) for x in np.arange(1, idx+1).tolist()))

with open('idx.dat', 'w') as f:
    	f.write(indeces)

subprocess.run(['mdconvert' , traj_in, '-a', 'idx.dat', '-o',  traj_out])


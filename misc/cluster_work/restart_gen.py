import subprocess
import glob
import os

# generates pdb from last snapshot of trajectory named traj_i.h5 and outputs traj_{i+2}.pdb

all_trajs = glob.glob('./*.h5')
latest_traj = max(all_trajs, key=os.path.getmtime)

i = latest_traj[-4]
restart = f'restart_{int(i)+1}.pdb'

subprocess.run(['mdconvert' , latest_traj, '-i -1', '-o',  restart])

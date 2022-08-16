#!/bin/bash
#SBATCH --time=03:00:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=64 

module purge
module load cuda

condapath=/work/LAS/potoyan-lab/davit/miniconda3

source $condapath/bin/activate $condapath/envs/md37

cd $PWD
python write_idx.py 0

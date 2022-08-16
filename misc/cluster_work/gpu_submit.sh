#!/bin/bash
#SBATCH --time=64:00:00   # walltime limit (HH:MM:SS)
#SBATCH --nodes=1   # number of nodes
#SBATCH --ntasks-per-node=1   # 36 processor core(s) per node
#SBATCH --gres=gpu:1
#SBATCH --partition=gpu    # gpu node(s)

module purge
module load cuda

# Run
cd $PWD
#source activate md37
/work/LAS/potoyan-lab/davit/miniconda3/envs/md37/bin/python mm_run.py

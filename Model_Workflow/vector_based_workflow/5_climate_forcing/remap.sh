#!/bin/bash
#SBATCH --account=rpp-kshook
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=10G
#SBATCH --time=03:00:00
#SBATCH --job-name=remap
#SBATCH --error=errors_BowAtLouise
#SBATCH --mail-user=some.example@something.ca
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END

module load StdEnv/2020
module load gcc

rm -rf $HOME/MESH-env
virtualenv --no-download $HOME/MESH-env 
source $HOME/MESH-env/bin/activate

pip install easymore

python3 2_easymore_remapping.py


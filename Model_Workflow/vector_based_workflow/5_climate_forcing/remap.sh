#!/bin/bash
#SBATCH --account=rpp-kshook
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=10G
#SBATCH --time=03:00:00
#SBATCH --job-name=remap
#SBATCH --error=errors_BowAtLouise
#SBATCH --mail-user=cooper.albano@usask.ca
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END

module load StdEnv/2020
module load gcc

source ~/easymore-env/bin/activate

pip install easymore

python3 2_easymore_remapping.py


#!/bin/bash
#SBATCH --account=rpp-kshook
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=1
#SBATCH --mem=30G
#SBATCH --time=01:00:00
#SBATCH --job-name=BowAtBanff
#SBATCH --error=errors
#SBATCH --mail-user=your.email@example.ca
#SBATCH --mail-type=BEGIN
#SBATCH --mail-type=END

mizufolder=/home/calbano/scratch/MESH-vector-simple-example/Model_Workflow/installs/MizuRoute/mizuRoute-main/route


# copy data into topology folder
cp $mizufolder/ancillary_data/param.nml.default ../workflow_data/domain_BowAtLouise/topology

# run mizuroute
$mizufolder/bin/MizuRoute $mizufolder/settings/BowAtLouise.control

# --- Code Provenance
# Copy this script into the input folder/_workflow_log/
mkdir $mizufolder/_workflow_log/
cp ./runMizuRoute.sh $mizufolder/_workflow_log/
# Create a log file
dt=$(date +'%Y%m%d')
echo "Copied param.nml.default into topology folder. ran mizuroute." >> $mizufolder/_workflow_log/$dt"_runMizuRoute.txt"

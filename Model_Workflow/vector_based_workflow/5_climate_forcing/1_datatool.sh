

cd 
#rm -rf $HOME/scratch/rdrs_output/
rm -rf datatool
git clone https://github.com/kasra-keshavarz/datatool # clone the repository
cd datatool

# Uncomment this section to install cdo and nco if working on a workstation machine. These packages are required. Must have sudo authority.
#sudo apt update
#sudo apt install cdo
#sudo apt install nco

./extract-dataset.sh  --dataset=RDRS \
  --dataset-dir="/project/rpp-kshook/Model_Output/RDRSv2.1" \
  --output-dir="/enter/path/to/MESH-vector-simple-example/Model_Workflow/forcing" \
  --start-date="1980-01-01 00:00:00" \
  --end-date="1980-12-31 00:00:00" \
  --lat-lims=51,52  \
  --lon-lims=-117,-116 \
  --variable="RDRS_v2.1_P_P0_SFC,RDRS_v2.1_P_HU_09944,RDRS_v2.1_P_TT_09944,RDRS_v2.1_P_UVC_09944,RDRS_v2.1_A_PR0_SFC,RDRS_v2.1_P_FB_SFC,RDRS_v2.1_P_FI_SFC" \
  --prefix="rdrsv2.1_" \
  --email="some.example@something.ca" \
  -j; # Remove this argument if not submitting to a scheduler on HPC cluster
  
  cd ../scratch


# -*- coding: utf-8 -*-
"""
NAME
    create_MESH_RFF_MizuRoute 
PURPOSE
    The purpose of this script is to read MESH extracted RFF, reorder it to be
    configurable and read by mizuroute, and finally save it in the NetCDF format
     
PROGRAMMER(S)
    Ala Bahrami
REVISION HISTORY
    20210628 -- Initial version created and posted online
    20221109 -- Applied some modifications to be addapble for NA workflow
    
    
See also 
     create_MESH_drainage_database   
    
REFERENCE 
    
"""
# %% import modules 
import numpy as np
import xarray as xs
import pandas as pd
import time 
from datetime import datetime
from pathlib import Path

#Control file handling
# Easy access to control file folder
controlFolder = Path('../0_control_files')

# Store the name of the 'active' file in a variable
controlFile = 'control_active.txt'

#Function to extract a given setting from the control file
def read_from_control( file, setting ):
     
    # Open 'control_active.txt' and ...
    with open(file) as contents:
        for line in contents:
             
            # ... find the line with the requested setting
            if setting in line and not line.startswith('#'):
                break
     
    # Extract the setting's value
    substring = line.split('|',1)[1]      # Remove the setting's name (split into 2 based on '|', keep only 2nd part)
    substring = substring.split('#',1)[0] # Remove comments, does nothing if no '#' is found
    substring = substring.strip()         # Remove leading and trailing whitespace, tabs, newlines
        
    # Return this value   
    return substring

#Function to specify a default path
def make_default_path(suffix):
     
    # Get the root path
    rootPath = Path( read_from_control(controlFolder/controlFile,'root_path') )
     
    # Get the domain folder
    #domainName = read_from_control(controlFolder/controlFile,'domain_name')
    #domainFolder = 'domain_' + domainName
     
    # Specify the forcing path
    defaultPath = rootPath / suffix
     
    return defaultPath

# Get the domain folder
domain_name = read_from_control(controlFolder/controlFile,'domain_name')
domainFolder = 'domain_' + domain_name

# Get the simulation dates
start_sim = read_from_control(controlFolder/controlFile, 'simulation_start')
end_sim = read_from_control(controlFolder/controlFile, 'simulation_end')

# Get RFF input
mizupath = read_from_control(controlFolder/controlFile,'mizu_RFF_input')
if mizupath == 'default':
    mizupath = make_default_path('vector_based_workflow/6_model_runs/')
else:
    mizupath = mizupath
print(mizupath)
# %% input files 
start_time = time.time()
input_topology     = f'../workflow_data/{domainFolder}/topology/network_topology_{domain_name}.nc' 
outdir             = f'../workflow_data/{domainFolder}/drainagedatabase/'

# %% Reading both network topology and drainage database
network_topo = xs.open_dataset(input_topology)
network_topo.close()

drainage_db = xs.open_dataset(outdir+domain_name+'_MESH_drainage_database.nc')
drainage_db.close()

# %% Seg_ids 
segid         = network_topo['seg_id'].values
segid_reorder = drainage_db['seg_id'].values

#%% Find reorder indices 
n = len(segid)
ind = []

for i in range(n):
    fid = np.where(segid_reorder == segid[i])[0]
    ind = np.append(ind, fid)

ind = np.int32(ind)  

# %% reading daily MESH runoff 
rff  = xs.open_dataset(str(mizupath)+'/results/RFF_D_GRD.nc')
rff.close()

rff_reorder = rff['RFF'].values[:,ind,0]

# convert MESH daily rff to mm/s
rff_reorder = rff_reorder/86400

# %% create netcdf rff dataset and write it as output 
# time index 
tt = pd.date_range(start=start_sim, end=end_sim, freq='D')

rff_ds = xs.Dataset(
    {
     "RUNOFF": (["time", "hru"], rff_reorder.astype(float)),
     },
    coords={
        "time" : (["time"], tt),
        "hru" : (["hru"], segid),
    },
)

# meta data attributes 
rff_ds['RUNOFF'].attrs.update(_FillValue = -999)
rff_ds['time'].encoding['calendar'] = 'standard'
rff_ds['time'].attrs.update(standard_name = 'time')
                            
now = datetime.now()
rff_ds.attrs['Conventions'] = 'CF-1.6'
rff_ds.attrs['License']     = 'Created by MESH vector-based workflow scripts'
rff_ds.attrs['history']     = 'Created ' + now.strftime('%Y/%m/%d %H:%M:%S')
rff_ds.attrs['featureType'] = 'timeSeries' 

# save the output 
comp = dict(zlib=True, complevel=6)
encoding = {var: comp for var in rff_ds}
rff_ds.to_netcdf(str(mizupath)+'/results/'+domain_name+'_distributed_default_timestep.nc', encoding=encoding)
print('--%s seconds--' %(time.time() - start_time))


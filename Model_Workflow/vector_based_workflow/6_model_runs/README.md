# Running MESH

## Input Files
The files present in this directory are the minimum requirements to run MESH.
The program will crash if any of these are not present, though there may be other accetable formats (see https://wiki.usask.ca/display/MESH/MESH+Input+Files for details).

### MESH_drainage_database.nc
This is the basin information file that is created from the network topology in the previous steps.
By default, it is stored in [root path]/vector_based_workflow/workflow_data/domain_[domain name]/drainagedatabase
The example shell script "BowAtLouise_MESH_RDRSV2.1.sh" will link this file to this folder. 

#### Note: Links to any of these files will suffice, but they must be present in this folder in some fashion.

### MESH_input_reservoir.txt
This file is similar to MESH_input_streamflow.txt. It can be used to represent natural or controlled reservoirs in the basin.
Even if no reserviors exist, this file must be present using dummy values of "0    0    0"
More information at https://wiki.usask.ca/display/MESH/MESH_input_reservoir.txt or https://wiki.usask.ca/display/MESH/MESH_input_reservoir.tb0

### MESH_input_run_options.ini
This file determines the options activated or deactivated for the model run.
Detailed information on this file and on many of the option flags is available here https://wiki.usask.ca/display/MESH/MESH_input_run_options.ini

### MESH_input_streamflow.ini
Much like the input reservior file, this file must be present regardless of whether any gauges exist in the basin.
Additionally, if no gauges exist, a dummy gauge must be used and given a non-zero value to initialize flow in the basin.
More info: https://wiki.usask.ca/display/MESH/MESH_input_streamflow.txt or https://wiki.usask.ca/display/MESH/MESH_input_streamflow.tb0

### MESH_input_soil_levels.txt
This file defines the number and depth of soil layers.
The first layer is the surface layer, which can be no less than 10 cm in depth. 
A minimum of three soil layers are required in the file.
https://wiki.usask.ca/display/MESH/MESH_input_soil_levels.txt

### MESH_parameters_CLASS.ini
This file defines the parameters for CLASS. 
There is a header section, followed by a unique section for each GRU
Please refer here to learn how to define CLASS parameters: 
https://wiki.usask.ca/display/MESH/MESH_parameters_CLASS.ini

### MESH_parameters_hydrology.ini
This file defines hydrology parameters for the basin.
Please refer here for details on how to set up this file:
https://wiki.usask.ca/pages/viewpage.action?pageId=1176797394
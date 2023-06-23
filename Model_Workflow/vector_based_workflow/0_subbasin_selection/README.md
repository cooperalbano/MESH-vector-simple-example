## Subbasin Selection
Subbasin selection using EASYMORE is depreciated. This script has been modified to select all upstream segments and subbasins from a designated outlet segment.

## Programmers
Ala Bahrami
Cooper Albano

## Description
This is an optional script to extract a smaller domain of interest from within a larger domain of discretized subbasins in a shapefile format. Once the 'Subbasin Selection Settings' have been specified in the control file, users can usually run the python script or jupyter notebook to produce the subsette shapefiles. If the default settings are used, the outputs will be located in 'root_path/shapefiles'. 

###### *Note: Depending on the size of the parent shapefiles, this script could take several minutes to complete. An information line reading "EASYMORE [version] initiated" will be printed to the terminal and will remain static until the script is complete.*

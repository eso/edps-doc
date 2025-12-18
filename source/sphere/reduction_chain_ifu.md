# The SPHERE data reduction flow.

The overall data flow of the SPHERE pipeline is displayed [here](figures/reduction_cascade.jpg).

The reduction cascade is organized in tasks, which represent well defined steps in the process. Tasks can be grouped
inside sub-workflows.
Each task runs a recipe; the detailed description of the algorithms,
input, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The `EDPS` workflow is designed to execute the tasks that deliver
the final reduced data cube for each dataset. It can be either the product of a single exposure, or the combination of
multiple exposures. Only calibrations needed by the selected the scientific exposures are processed.

It is possible to set `EDPS` to perform the data reduction until a certain step of the reduction chain (e.g. to reduce
only standard stars, or only flat fields).
This is done by specifying the desired tasks in the field `Select reduction target` of the `Raw Data` tab.

The reduction steps are:

## 1. Subworkflow Master Dark**

### 1a. Create Master Dark**

recipe: `sph_ifs_master_dark`

This recipe creates a master dark calibration frame 
by combining raw dark exposures using a specified 
collapse algorithm.

**Customization**

Recipe parameters:
- The collapse algorithm is set by the parameter
`coll_alg`. 
Its default value *clean_mean* (parameter value *2*), 
can be changed to *mean* (*0*) or *median* (*1*).

### 1b. Identify Bad Pixels*

recipe: `sph_ifs_master_dark`

Bad pixels are identified on the Master Dark 
using thresholding, smoothing to remove large-scale variations, 
and sigma clipping. 
The outputs: the bad-pixel and input-pixel counts, 
are stored in different extensions of the
Master Dark. 
A separate hot-pixel map is also written out.

**Customization**

Recipe parameters:
- Parameter `sigma_clip` (default = 5.0) controls the sigma
clipping value for static badpixel detection.

### 1c. Create Master Dark**

recipe: `sph_ifs_cal_background`

### 1d. Create Master Dark**

recipe: `sph_ifs_cal_background`


## Spectral Positions

**Add description**


---
Go to SPHERE EDPS tutorial [index](../sphere/index)
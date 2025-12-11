## The EFOSC spectroscopic data reduction flow.

The overall data flow of the EFOSC spectroscopic pipeline is displayed [here](figures/reduction_cascade_spc.jpg).

The reduction cascade is organized in tasks, which represent well defined steps in the process. Tasks can be grouped
inside sub-workflows.
Each task runs a recipe; the detailed description of the algorithms,
input, outputs and recipe parameters used in each recipe are available
in the pipeline manual. Here, we present only the description of most
important features.

The `EDPS` workflow is designed to execute the tasks that deliver
the final reduced spectra cube for each dataset. Only calibrations needed by the selected the scientific exposures are processed.

It is possible to set `EDPS` to perform the data reduction until a certain step of the reduction chain (e.g. to reduce
only standard stars, or only flat fields).
This is done by specifying the desired tasks in the field `Select reduction target` of the `Raw Data` tab.

The reduction steps are:

###  Bias subtraction

The task **bias** runs the recipe **efosc_bias** to generate a MASTER_BIAS calibration.
Typicall, default recipe parameters deliver good results. 


### Second step

**Add description**


---
Go to SPHERE EDPS tutorial [index](../sphere/index)
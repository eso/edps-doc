# Configure a dataset

Before creating a dataset, the user has the possibility to 
specify the preferences of the calibrations to associate, and - if the workflow foresees it - configure the 
workflow parameters to select the reduction strategies 

## Select the desired reduction target
The "Reduction Target", or the "target task" is the end point of the reduction cascade. When specifying a target, EDPS will process
all and only the files needed to execute it. For example, if my target is "science", and the science files
need the bias files, EDPS will process only the biases that have been selected to process those science files; then it 
processes the science using the product of the bias reduction.
However, if my target is bias, then EDPS will process all and only the bias files, regardless they are not used by any science. 
In this case, EDPS does not process the science, as it has reached already the end reduction point (e.g., process all biases).
The "Target category" is a group of target that have similar purposes. For example, the target category "science", includes
all the tasks that deliver final scientific products, the target category "qc1calib" includes all and only the tasks that 
processes calibrations (e.g., bias, standard stars).

For scientific data reduction purposes, leave the default Target Category and Reduction Targets. 

## Select appropriate calibrations
```{include} ../common/appropriate_calibrations.md
```



